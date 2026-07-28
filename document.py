import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Hugging Face Endpoint
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

# Chat Model
model = ChatHuggingFace(llm=llm)

# Prompt
prompt = PromptTemplate(
    template="Write a summary for the following poem:\n\n{poem}",
    input_variables=["poem"],
)

# Output Parser
parser = StrOutputParser()

# Load the text file
loader = TextLoader("document.txt", encoding="utf-8")
docs = loader.load()

# Check the loaded document
print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

# Create the chain
chain = prompt | model | parser

# Invoke the chain
result = chain.invoke({"poem": docs[0].page_content})

print("\nSummary:\n")
print(result)
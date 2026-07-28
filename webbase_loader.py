import os
from langchain_community.document_loaders import WebBaseLoader
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
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

# Output Parser
parser = StrOutputParser()


url = 'https://www.flipkart.com/search?q=iphone+17&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone+17%7CMobiles&requestId=c8d96aa2-985a-4821-966e-016657f64ce7&as-searchtext=iphone%2017'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser
print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))
print(chain.invoke({'question':'What is the price of iphone 17 ?', 'text':docs[0].page_content}))
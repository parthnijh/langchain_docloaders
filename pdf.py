from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
parser=StrOutputParser()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash",api_key=os.getenv("GEMINI_API_KEY"))
loader=PyPDFLoader("revised 2025 Guidelines_Programming using C++.pdf")
docs=loader.load()
prompt=PromptTemplate(template="i cant read all of these explain these guidelines to me {guidelines}",
                      input_variables=["guidelines"])
chain=prompt | model | parser 
result=chain.invoke({"guidelines":docs[1].page_content})
print(result)
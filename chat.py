import fastapi
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
import os
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    user_id: str
    query: str

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URI = os.getenv("URI")

user_id = "user123"

client = MongoClient(URI)
db = client["Chatbot"]
collection = db["Chatbot"]

def get_history(user_id):
  chats=collection.find({"userid":user_id}).sort("_id", -1).limit(5)
  history=[]
  for chat in chats:
    history.append(("user", chat["query"]))
    history.append(("assistant", chat["response"]))
  return history


@app.get("/")
def home():
    return {"message": "Hey! Nice to meet you"}

@app.post("/query")
def handle_query(query: Query):
    user_query = query.query
    user_id = query.user_id
    history = get_history(user_id)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a study assistant that helps users ask question related to study topics"),
        ("placeholder", "{history}"),
        ("user", "{input}")
    ])
    llm = ChatGroq(
        api_key=GROQ_API_KEY, 
        model="llama-3.3-70b-versatile",
        temperature=0.5 
    )
    chain = prompt | llm 
    response = chain.invoke({"history": history, "input": user_query})
    data_to_store = {
        "userid": user_id,
        "query": user_query,
        "response": response.content
    }
    result = collection.insert_one(data_to_store)
    return {"response": response.content}


"""while True:
 user_query = input("Enter your query: ")
 history = get_history(user_id)
 
 if user_query.lower() == "exit":
    break
 


 prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant answering questions about programming."),
    ("placeholder", "{history}"),
    ("user", "{input}")
 ])

 llm = ChatGroq(
    api_key=GROQ_API_KEY, 
    model="llama-3.3-70b-versatile",
    temperature=0.5 
 )

 chain = prompt | llm 

 response = chain.invoke({"history": history, "input": user_query})

 print(response.content)

 data_to_store = {
    "userid": user_id,
    "query": user_query,
    "response": response.content
 }

 result = collection.insert_one(data_to_store)"""

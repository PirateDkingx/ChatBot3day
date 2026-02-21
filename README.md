Study Bot: AI-Powered Study Assistant
This project is an AI-powered chatbot designed to help users with academic and learning-related questions. It features a conversational memory system that allows it to remember previous interactions for contextual responses.

For Testing heres my fastapi url- http://98.88.247.78:8000/docs 
(It is hosted on aws cloud it will be only be available for a week after the release of project )

🚀 Features

Context-Aware Responses: Remembers previous parts of the conversation to provide better assistance.


Academic Focus: Specialized system logic to handle study topics.


Persistent Memory: Uses MongoDB to store and retrieve chat history.


API Ready: Built as a FastAPI application for easy integration.


🛠️ Tech Stack

Language: Python 


Framework: FastAPI 


AI Orchestration: LangChain & LangChain Groq 


Database: MongoDB (Atlas/Local) 



Deployment: Render 

📋 Prerequisites
Before running the project, ensure you have the following:

Python installed on your system.

A MongoDB URI (Local or MongoDB Atlas).


An LLM API Key (e.g., Groq API Key).


⚙️ Setup Instructions
1. Environment Variables
Create a .env file in the root directory and add your credentials:

GROQ_API_KEY=your_api_key_here
MONGO_URI=your_mongodb_uri_here

2. Installation
   
Install the necessary Python packages:

pip install -r requirements.txt


🧠 Overview
Product managers juggle a range of tasks—requirement gathering, roadmap planning, generating user stories, and stakeholder communication. What if an AI assistant could automate the repetitive parts and support decision-making intelligently?

This project introduces an AI-powered Product Manager Assistant built using LangChain, Google Gemini, and FastAPI, designed to streamline PM workflows through a set of smart REST APIs. It runs in a Dockerized environment for easy setup and extensibility.

💡 What You’ll Learn
How to orchestrate AI agents using LangChain for domain-specific tasks

How to expose AI functionality via REST APIs using FastAPI

How to deploy AI apps using Docker and manage secrets securely

Practical use cases of LLMs in product management and automation

⚙️ Key Features
🧠 LLM-powered agent workflows using LangChain + Gemini

🔗 Modular and extensible orchestration of product management tasks

🔧 FastAPI backend with interactive Swagger UI for easy testing

🐳 Fully containerized via Docker and Docker Compose

🔐 Environment variable-based API key management

🛠️ Setup Instructions
Prerequisites
Docker and Docker Compose installed

A Gemini API key (or other LLM API key)

Installation
Clone the repo:


git clone https://github.com/saitej13sai/AI-Product-Manager-Assistant.git
cd AI-Product-Manager-Assistant
Create a .env file with your API key:

env

GEMINI_API_KEY=your-api-key-here
Run the app:


docker-compose up --build
The Swagger UI will be available at: http://localhost:8000/docs


📌 Why This Project Matters
This assistant is not just a demo—it's a foundation for AI-native product tools. It proves how LLMs can:

Automate tedious documentation tasks

Support product decisions with reasoning

Create structured output from natural input

Whether you’re a product manager, engineer, or AI enthusiast, this project showcases how to deploy AI in impactful, real-world scenarios.



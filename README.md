# 🤖 AI Product Manager Assistant

An **AI-powered assistant** designed to help product managers with task automation, decision support, and intelligent recommendations.

Built using **FastAPI**, orchestrated **AI agents via LangChain**, and integrated with **Gemini LLMs**, this project exposes REST APIs wrapped in a Dockerized environment for fast, portable deployment.

---

## 🚀 Project Overview

Product managers face constant pressure to deliver quickly while managing complex product workflows, communicating across teams, and making informed decisions.

This assistant solves those challenges using **LLM-based automation**—generating user stories, drafting product requirements, suggesting roadmaps, and offering intelligent insights—all through simple API calls.

It’s a real-world example of how **AI can accelerate modern product development**.

---

## ⚙️ Features

✅ AI-driven product management assistant powered by LLMs  
✅ REST API with interactive **Swagger UI** for exploration and testing  
✅ Agent orchestration via **LangChain** for modular, extensible workflows  
✅ Containerized deployment with **Docker & Docker Compose**  
✅ Secure **.env-based API key management** for sensitive credentials  

---

## 🧠 How It Works

This assistant uses LangChain agents to perform specialized tasks based on user prompts. These agents interact with LLMs like **Gemini** to perform natural language understanding, generate content, and structure output that’s actionable for product teams.

### 🛠️ Key Capabilities:
- **Requirement Gathering** – Generate product requirements from a feature description  
- **User Story Generation** – Convert a feature idea into detailed Agile user stories  
- **Roadmap Suggestions** – Recommend next steps or feature sequencing  
- **Decision Support** – Provide pros/cons or data-driven insights using reasoning-capable models  

---

## 📦 Getting Started

### ✅ Prerequisites
- [Docker](https://www.docker.com/) & Docker Compose installed
- A Gemini API key (or swap in your preferred LLM API key)

### 🔧 Setup

```bash
# 1. Clone the repository
https://github.com/saitej13sai/AI-Product-Manager-Assistant
cd AI-Product-Manager-Assistant

# 2. Create a .env file with your API key
echo "GEMINI_API_KEY=your-api-key-here" > .env

# 3. Run the application
docker-compose up --build



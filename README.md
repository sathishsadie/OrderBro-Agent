# 🧠 OrderBro AI Agent (LLM + MCP + Backend API)

## 📌 Project Overview

OrderBro AI Agent is an intelligent conversational ordering assistant built using **LLM agents + MCP (Model Context Protocol)** that can interact with a real backend ordering system.

Instead of manually navigating an application or dashboard, users can simply **chat in natural language** to:

* Browse products
* Check friends available for ordering
* Place orders to friends
* Track pending orders
* Cancel orders

The agent understands user intent and calls backend APIs automatically through tools.

---

## 🚨 Problem This Project Solves

Most internal ordering / task delegation systems suffer from:

* Too many UI clicks
* Hard navigation
* Users not knowing where a feature exists
* Time wasted searching products or assigning tasks
* Non‑technical users struggling with dashboards

### Traditional Flow

User → UI → Find Shop → Find Product → Select Friend → Place Order → Track Order

### With OrderBro AI Agent

User → Chat → Done ✅

The AI converts natural language into backend actions.

Example:

> "Send 2 coffees to Arjun"

The agent:

1. Finds products
2. Finds friend
3. Creates order
4. Confirms back to user

No manual interaction required.

---

## 🧱 System Architecture

User Chat
↓
LLM Agent (Gemini)
↓
MCP Tools Layer
↓
Python MCP Server
↓
Backend OrderBro REST API
↓
Database

---

## 🧠 How the Agent Works (Important for Interviews)

This project uses **Tool‑Using AI Agent Architecture**.

The LLM does NOT directly access database or APIs.
Instead, it calls "tools".

### Step 1 — User Intent Understanding

Gemini model reads message and decides action.

Example intents:

* Show products
* Give order
* Cancel order
* Check pending orders

### Step 2 — Tool Selection (MCP)

The agent chooses one of the tools:

| Tool                     | Purpose          |
| ------------------------ | ---------------- |
| fetch_available_products | Get all products |
| available_users          | Get friends      |
| give_order_to_friend     | Place order      |
| ordered_me               | Pending orders   |
| cancel_order             | Cancel order     |

### Step 3 — MCP Server Executes API

The MCP server converts tool calls → REST API calls.

Example:
LLM says → give_order_to_friend
Server calls → POST /orders/me

### Step 4 — Response Returned to LLM

LLM converts raw JSON → human readable message.

---

## 📂 Project Files Explanation

### `agent.py`

Creates the intelligent AI agent.

Responsibilities:

* Loads Gemini model
* Connects MCP client
* Contains system prompt rules
* Decides which tool to call

This is the "brain" of the system.

---

### `server.py`

Acts as the **bridge between AI and Backend**.

It exposes tools to the agent and calls backend APIs.

Example:
AI → cancel_order(order_id)
Server → POST /orders

This is the "hands" of the system.

---

### `.env`

Contains configuration variables:

* API URL
* Auth token
* User ID
* Gemini API key

Never commit this file to GitHub.

---

## ⚙️ Environment Variables (.env)

```
GOOGLE_API_KEY=your_gemini_key
ORDERBRO_API_URL=http://127.0.0.1:8000/
ORDERBRO_TOKEN=your_backend_token
ORDERBRO_USER_ID=15
```

---

## ▶️ How To Run The Project (Local Setup)

### 1️⃣ Install Requirements

```
pip install strands mcp python-dotenv requests
```

(Also install backend dependencies if needed)

---

### 2️⃣ Start Backend API

Make sure OrderBro backend is running:

```
http://127.0.0.1:8000/
```

---

### 3️⃣ Start MCP Server

```
python server.py
```

This exposes tools to the AI.

---

### 4️⃣ Run AI Agent

Open new terminal:

```
python agent.py
```

Now you can chat with the agent.

---

## 💬 Example Queries

```
What products are available?
Show my pending orders
Send 2 tea to Rahul
Cancel order 24
Who can receive my order?
```

---

## 📊 What Insights This Project Demonstrates

This project proves understanding of:

### AI Concepts

* Tool‑calling agents
* LLM reasoning control
* Prompt engineering
* Deterministic workflows
* Function calling architecture

### Backend Concepts

* API integration
* Service orchestration
* Authentication flow
* Request validation

### System Design

* AI → Tool → API → Database pipeline
* Decoupled architecture
* Safe AI actions (no hallucinations)

---

## ⭐ Key Features

* No hallucination AI (always uses tools)
* Deterministic execution
* Natural language control over backend
* Production‑style agent architecture
* Extensible tool framework

---

## 🧪 Future Improvements

* Multi‑user session memory
* Voice ordering
* Order recommendations
* Analytics dashboard
* Autonomous scheduled ordering

---

## 🏁 Conclusion

OrderBro AI Agent demonstrates how Large Language Models can be safely integrated with real systems using MCP tools to perform real actions — not just answer questions.

It converts conversation into transactions.

This is the foundation of real‑world AI assistants used in enterprise automation systems.

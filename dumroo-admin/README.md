# Dumroo Admin Panel – AI-Powered Natural Language Query System

**An intelligent admin dashboard where teachers ask questions in plain English and get instant, filtered student data — with role-based access control.**

> **Assignment Goal:** Demonstrate AI + NLP + Role-Based Access in a real-world education panel  
---

## Features

| Feature | Status |
|-------|--------|
| Natural language queries (English → Data) | Working |
| Role-based access (Admin sees only their grade) | Working |
| Real-time answers using **Groq + Llama 3.1** | Working |
| Secure scoping: No access to other grades | Working |
| Export results to CSV | Working |
| Modular code (ready for real database) | Working |
| Streamlit UI | Working |

---

## Tech Stack

- **Python** 3.11
- **Streamlit** – Interactive UI
- **Pandas** – Data handling
- **LangChain + Groq** – AI query engine
- **Llama 3.1 8B** (`llama-3.1-8b-instant`) – Fast, free, reliable
- **CSV** – Sample dataset

---

## Setup (Takes 2 Minutes)

```bash
git clone https://github.com/Sumit6307/dumroo-admin.git
cd dumroo-admin

python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt











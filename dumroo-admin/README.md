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

## Setup 

```bash
git clone https://github.com/Sumit6307/Dumroo-Assignment.git
cd dumroo-admin

python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Mac/Linux


pip install -r requirements.txt



#,Query to Type

1,Which students haven’t submitted their homework yet?
2,Show me quiz scores from last week
3,Show me performance data for last week
4,List all students in Grade 7
5,Who scored below 80 in quizzes?
6,Students in Class A
7,List students who submitted homework
8,Show quiz scores from November 
9,Who has the highest quiz score?
10,List all upcoming quizzes for next week










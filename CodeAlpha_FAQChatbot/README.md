# 🤖 FAQ Chatbot

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![Domain](https://img.shields.io/badge/Domain-Artificial%20Intelligence-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

> **CodeAlpha AI Internship | Project 6 of 6**

---

## 📌 Overview

An intelligent FAQ chatbot built with Streamlit and NLP techniques. The bot takes a user's natural language question, vectorizes it using TF-IDF, and uses Cosine Similarity to find and return the most relevant pre-defined FAQ answer — no large language model or paid API required.

---

## 🎯 Objective

Build a lightweight, NLP-powered FAQ chatbot that intelligently matches user queries to the most relevant answer from a curated knowledge base.

---

## 📂 Project Structure

```
CodeAlpha_FAQChatbot/
├── faq_chatbot.py               # Main Streamlit chatbot app
├── faqs.json / faqs.py          # FAQ knowledge base (questions + answers)
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| Streamlit | Interactive web UI |
| Scikit-learn | TF-IDF Vectorization |
| NumPy | Cosine similarity computation |

---

## ✨ Features

- **Natural Language Input** — Users type questions in plain English
- **TF-IDF Vectorization** — Converts text to numerical feature vectors
- **Cosine Similarity Matching** — Finds the closest FAQ to the user's query
- **Threshold-Based Response** — Returns "I don't know" for low-confidence matches
- **Persistent Chat History** — Conversation displayed as a scrollable chat log
- **Streamlit UI** — Clean, real-time interactive interface

---

## 🔬 How It Works

```
User Question
     ↓
TF-IDF Vectorizer (fit on FAQ questions)
     ↓
Cosine Similarity vs all FAQ vectors
     ↓
Best Match Score > Threshold?
   YES → Return matched answer
   NO  → Return fallback response
```

---

## 🚀 How to Run

```bash
cd CodeAlpha_FAQChatbot

# Install dependencies
pip install -r requirements.txt

# Launch the chatbot
streamlit run faq_chatbot.py
```

Open your browser at `http://localhost:8501`

---

## 📚 Key Learnings

- TF-IDF vectorization and text similarity
- Information retrieval vs generative AI approaches
- Streamlit session state for chat history
- Building production-ready NLP applications without LLMs

---

*Developed as part of the CodeAlpha Internship Program — Ameena Quadri*

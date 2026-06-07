# 🌐 Language Translation Tool

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Deep Translator](https://img.shields.io/badge/deep--translator-1.11+-yellow.svg)
![Domain](https://img.shields.io/badge/Domain-Artificial%20Intelligence-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

> **CodeAlpha AI Internship | Project 5 of 6**

---

## 📌 Overview

An interactive web application built with Streamlit that enables real-time text translation between multiple languages. The tool leverages the `deep-translator` library to provide accurate, fast translations with an intuitive user interface — no API key required.

---

## 🎯 Objective

Develop a user-friendly, multilingual translation tool as a Streamlit web app, demonstrating NLP API integration and interactive application development.

---

## 📂 Project Structure

```
CodeAlpha_LanguageTranslator/
├── language_translator.py       # Main Streamlit app
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| Streamlit | Web application framework |
| deep-translator | Translation engine (Google Translate API wrapper) |

---

## ✨ Features

- **Multi-language support** — Translate between 100+ languages
- **Automatic language detection** — Detect source language automatically
- **Real-time translation** — Instant output as you type or submit
- **Clean UI** — Simple, accessible Streamlit interface
- **Error handling** — Graceful messages for unsupported inputs

---

## 🔬 How It Works

1. User enters text in the input box
2. User selects target language from dropdown
3. `deep-translator` calls Google Translate under the hood
4. Translated text is displayed instantly in the output panel

---

## 🚀 How to Run

```bash
cd CodeAlpha_LanguageTranslator

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run language_translator.py
```

Open your browser at `http://localhost:8501`

---

## 📸 App Preview

The app provides a two-panel layout: source text input on the left, translated output on the right, with a language selector dropdown.

---

## 📚 Key Learnings

- Streamlit app development and deployment
- Third-party translation API integration
- UX design principles for AI tools
- Language detection with NLP libraries

---

*Developed as part of the CodeAlpha Internship Program — Ameena Quadri*

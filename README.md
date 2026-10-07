# 🚀 LinkedIn Post Generator

An AI-powered LinkedIn Post Generator built using **Python, Streamlit, LangChain, and Groq LLM**.

The application helps users quickly generate professional and engaging LinkedIn posts based on a selected topic, post length, and language.

---

## 📌 Project Overview

The **LinkedIn Post Generator** is an AI-based web application designed to simplify the process of creating high-quality LinkedIn content.

Users can select:

- 🏷️ Topic
- 📏 Post Length
- 🌐 Language

Based on these selections, the application generates a professional LinkedIn post using an AI language model.

---

## ✨ Features

- 🤖 AI-powered LinkedIn post generation
- 🏷️ Multiple topic selection
- 📏 Short, Medium, and Long post lengths
- 🌐 English and Hinglish language support
- 🎨 Interactive Streamlit user interface
- ⚡ Fast AI response using Groq
- 🧠 LangChain-based prompt processing
- 📚 Few-shot examples for better post generation
- 🔐 API key protection using environment variables

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Web application interface |
| LangChain | LLM integration and prompt handling |
| Groq | AI/LLM inference |
| Llama / GPT OSS | Large Language Model |
| Pandas | Data processing |
| Git & GitHub | Version control |
| python-dotenv | Environment variable management |

---

## 🏗️ Project Structure

```text
LinkedIn_post_generator/
│
├── data/
│   ├── processed_posts.json
│   └── raw_posts.json
│
├── few_shot.py
├── llm_helper.py
├── main.py
├── post_generator.py
├── preprocess.py
├── requirements.txt
├── .gitignore
└── README.md

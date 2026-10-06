# The AI-Proof Software Engineer 🚀
## A Senior Developer's Roadmap to Mastering GenAI, RAG, and Production-Grade AI Systems

Welcome to the official companion code repository for **"The AI-Proof Software Engineer"** by Vivek Chauhan. 

This repository is designed to accompany the book's station-by-station roadmap, taking you from the core foundations of large language models to deploying production-grade, hybrid-search Retrieval-Augmented Generation (RAG) systems.

---

## 🗺️ How to Use This Repository

This code is structured to follow the **12-Station Learning Path** detailed in the book. Instead of looking at a single massive codebase, treat each directory as a hands-on milestone:

1. **Read the Station:** Understand the architectural concepts, data paradigms, and system design trade-offs inside the book chapter.
2. **Run the Code:** Navigate to the corresponding folder in this repository, inspect the code blocks, and run them locally.
3. **Modify & Experiment:** Tweak parameters (like model temperatures, chunking strategies, or vector weights) to build robust engineering intuition.

---

## 🛠️ Local Installation & Setup

To get these code samples running on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com
cd the-ai-proof-software-engineer
```

### 2. Set Up a Virtual Environment
As emphasized in **Station 3**, always isolate your dependencies to prevent version conflicts:

```bash
# Create the environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate
```

### 3. Install Required Libraries
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Your Environment Variables
For chapters interacting with hosted models (such as Station 7 and beyond), copy the template file and insert your private API keys:

```bash
cp station_07_llm_apis/.env.example .env
```
*Note: Never commit your actual `.env` file or raw keys to GitHub.*

---

## 📁 Repository Structure Map

*   `station_02_python_basics/` - Quick verification scripts for environment setups and baseline package testing.
*   `station_03_ml_dl_foundations/` - PyTorch tensor basics, forward passes, and automatic gradient tracking mechanics.
*   `station_07_llm_apis/` - Real-world API configurations, token optimization trackers, and production Server-Sent Events (SSE) streaming architectures.
*   `data/` - Clean sample text assets to safely test your local vector ingestion pipelines.

---

## ⚖️ License

All code snippets and practical guides contained within this repository are licensed under the **MIT License**. Feel free to use, modify, and integrate these patterns into your personal or enterprise engineering projects.

---

## 📖 Get the Book
If you don't have a copy of the roadmap yet, you can pick up **The AI-Proof Software Engineer** here:
*   [Gumroad Bookstore Store Link]
*   [Amazon Kindle Worldwide Link]

For feedback, questions, or issues with code blocks, feel free to open an Issue or reach out directly at **iamchauhan.mca@gmail.com**.

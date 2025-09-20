# 💬 Conversational Analytics Assistant

This project lets you **ask natural language questions about your dataset** and get answers with **charts + summaries**.  


## 🚀 Features
- Natural language → pandas query
- Supports aggregations (sum, average, count)
- Auto-generates bar, line, or pie charts
- Example dataset included


## ⚙️ Installation
```bash
git clone https://github.com/yourusername/conversational-analytics-assistant.git
cd conversational-analytics-assistant
pip install -r requirements.txt
```

## ▶️ Usage
```
python src/pipeline.py --file data/sample_dataset.csv --query "What is the average income by city?"
```

Output:

Answer in text

Chart saved in assets/


## 📊 Tech Stack

Python

NLP: spaCy or regex-based parsing

Data handling: pandas

Visualization: matplotlib, seaborn

(Future: LLM via OpenAI / LangChain)


## 📌 Roadmap

 Add Streamlit UI for interactive chat

 Support multi-step questions

 Connect to SQL databases

 ## Requirements 
```txt
pandas
spacy
matplotlib
seaborn
pytest
```

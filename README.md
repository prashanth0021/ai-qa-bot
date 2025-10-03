# AI Q&A Bot 🤖

A very simple **AI-powered Q&A Bot** built as part of a motivation test project.  
The bot runs in the **command-line**, where users can type a question and get an answer using OpenAI/Hugging Face APIs.  

---

## 🚀 Part 1: Setup

1. Install **Python 3.10+**
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate    # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

---

## 🛠️ Part 2: Task

Run in terminal:
```bash
python app.py
```

---

## 🎯 Part 3: Stretch Goal

Run the UI version with:
```bash
streamlit run streamlit_app.py
```

---

## ✅ Tech Stack
- Python
- OpenAI API
- Streamlit (optional UI)

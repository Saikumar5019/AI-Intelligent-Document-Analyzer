# 📄 AI Intelligent Document Analyzer

An AI-powered document analysis system that processes PDF and image documents, extracts text using OCR, classifies document types, generates summaries, extracts key entities, performs risk analysis, and produces structured reports using Google Gemini.

---

## 🚀 Features

* Upload PDF and image documents
* Text extraction from PDFs
* OCR-based text extraction from scanned images using Tesseract OCR
* AI-powered document classification
* Automatic document summarization
* Key entity extraction
* Risk assessment and flagging
* Structured JSON report generation
* Interactive Streamlit dashboard
* Downloadable analysis reports

---

## 🏗️ Architecture

```text
Streamlit UI
      ↓
Document Upload
      ↓
PDF Parser / Tesseract OCR
      ↓
Text Extraction
      ↓
Google Gemini
      ↓
Document Classification
      ↓
Summary Generation
      ↓
Entity Extraction
      ↓
Risk Analysis
      ↓
JSON Report
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### OCR & Document Processing

* Tesseract OCR
* pdfplumber
* Pillow

### AI & LLM

* Google Gemini 2.5 Flash
* LangChain

### Backend

* Python

### Configuration

* python-dotenv

---

## 📂 Project Structure

```text
AI-Document-Analyzer/

│
├── app.py
│
├── parser/
│   ├── pdf_parser.py
│   └── image_parser.py
│
├── prompts/
│   ├── classify_prompt.py
│   ├── summary_prompt.py
│   └── risk_prompt.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI-Document-Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Get your API key from Google AI Studio.

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📊 Output

The application provides:

* Document Type Classification
* Executive Summary
* Key Entity Extraction
* Risk Assessment
* Structured JSON Report

---

## 🎯 Use Cases

* Invoice Analysis
* Contract Review
* Resume Screening
* Medical Report Analysis
* Bank Statement Processing
* Automated Document Understanding

---

## 🔮 Future Enhancements

* Multi-document comparison
* PDF report generation
* RAG-based document search
* Multi-language OCR support
* Document chat assistant
* Advanced compliance checking

---

## 👨‍💻 Author

BATTAMEKALA SAI KUMAR

Data Science | Machine Learning | Generative AI

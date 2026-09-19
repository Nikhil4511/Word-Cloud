# Word-Cloud


# ☁️ WordCloud Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-1.39.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/NLP-WordCloud-8A2BE2?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  A multi-format text analysis web app that generates word clouds and frequency tables from <strong>TXT, PDF, and DOCX</strong> files — with real-time stopword control, word search, and export options.
</p>

---

## 📌 Table of Contents

- [Overview](#overview)
- [Live Demo](#live-demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [App Screenshots](#app-screenshots)
- [Key Learnings](#key-learnings)
- [Author](#author)

---

## 🔍 Overview

This project is a fully interactive **NLP-powered text analysis tool** built with Streamlit. Users can upload any text-heavy file — a resume, research paper, book chapter, or report — and instantly visualize word frequency as a word cloud along with a filterable frequency table.

It showcases end-to-end skills in:
- Multi-format file parsing (TXT, PDF, DOCX)
- Natural Language Processing (stopword removal)
- Data visualization (Matplotlib + WordCloud)
- Building and deploying production-ready Streamlit apps

---

## 🚀 Live Demo

> 🔗 **[Try the App Live](#)** ← *(Replace with your Streamlit Cloud / Hugging Face Spaces link)*

![App Demo](assets/demo.gif) <!-- Add a screen recording GIF here -->

---

## ✨ Features

| Feature | Details |
|---|---|
| 📁 **Multi-format Upload** | Supports `.txt`, `.pdf`, and `.docx` files |
| ☁️ **Word Cloud Generation** | Visual cloud of most frequent words |
| 🎛️ **Customizable Dimensions** | Adjust width & height via sidebar sliders |
| 🚫 **Stopword Filtering** | Toggle standard stopwords + add custom ones |
| 📊 **Word Frequency Table** | Sortable table of all word counts |
| 🔍 **Word Search** | Instantly look up any word's frequency |
| 📥 **Download Options** | Export word cloud as PNG/JPG; frequency table as CSV |
| ⚡ **File Info Display** | Shows filename, type, and size on upload |

---

## 🛠️ Tech Stack

| Layer | Technology | Version |
|---|---|---|
| Language | Python | 3.10+ |
| Web App | Streamlit | 1.39.0 |
| Data Handling | Pandas, NumPy | 2.2.2 / 1.26.4 |
| Visualization | Matplotlib | 3.9.2 |
| NLP / Word Cloud | wordcloud | 1.9.3 |
| PDF Parsing | PyPDF2 | 3.0.1 |
| DOCX Parsing | python-docx | 1.1.2 |
| Version Control | Git & GitHub | — |

---

## 📁 Project Structure

```
wordcloud-generator/
│
├── wordcloud_app.py         # Main Streamlit application
├── requirements.txt         # Python dependencies
├── assets/
│   └── demo.gif             # App demo GIF (add yours here)
└── README.md                # Project documentation
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wordcloud-generator.git
cd wordcloud-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run wordcloud_app.py
```

App opens at `http://localhost:8501`

---

### 📦 requirements.txt

```
streamlit==1.39.0
pandas==2.2.2
numpy==1.26.4
matplotlib==3.9.2
wordcloud==1.9.3
python-docx==1.1.2
PyPDF2==3.0.1
```

---

## 🔄 How It Works

```
Upload File (.txt / .pdf / .docx)
         │
         ▼
   Parse & Extract Text
  (read_file / read_pdf / read_docx)
         │
         ▼
   Apply Stopword Filtering
  (Standard STOPWORDS + Custom picks)
         │
         ▼
  ┌──────┴──────────┐
  ▼                 ▼
Word Cloud      Word Frequency
  Image            Table (CSV)
  (PNG/JPG)      + Word Search
```

### File Parsing Logic

| File Type | Library Used | Method |
|---|---|---|
| `.txt` | Built-in | `file.getvalue().decode("utf-8")` |
| `.pdf` | PyPDF2 | `PdfReader` → extract text per page |
| `.docx` | python-docx | `Document` → join all paragraphs |

---

## 📸 App Screenshots

> *(Add screenshots here after running the app)*

| Upload & File Info | Generated Word Cloud |
|---|---|
| ![upload](assets/upload.png) | ![wordcloud](assets/wordcloud.png) |

| Word Frequency Table | Word Search |
|---|---|
| ![table](assets/table.png) | ![search](assets/search.png) |

---

## 💡 Key Learnings

- Parsing multiple file formats (PDF, DOCX, TXT) using dedicated Python libraries
- Implementing NLP stopword removal with dynamic user control via Streamlit sidebar
- Generating and customizing `WordCloud` visualizations with Matplotlib
- Creating in-browser file download links using `base64` encoding — no server storage needed
- Building a clean, sidebar-driven UI layout in Streamlit with sliders, multiselects, and checkboxes


## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ by Nikhil Pal | ⭐ Star this repo if you found it useful!
</p>

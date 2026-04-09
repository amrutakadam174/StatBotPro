# 📊 StatBot Pro – AI Data Analyst

StatBot Pro is an AI-powered data analysis web application built using **Streamlit** and **Pandas**.  
It allows users to upload datasets and interact with them using natural language queries.

---

## 🚀 Features

- Upload CSV datasets  
- Natural language queries  
- Statistical analysis (mean, max, min, sum)  
- Graph generation  
- Smart query handling (fuzzy + synonyms)  
- Secure query validation  
- Chat interface with history  
- Auto insights generation  
- Downloadable report  

---

## 🧠 Tech Stack

- Python  
- Streamlit  
- Pandas  
- Matplotlib  
- Difflib  

---

## 📅 Project Breakdown

---

### 🟢 Week 1 – Basic Data Analysis

**Objective:**  
Build a system to analyze datasets using simple queries.

**Features:**

- CSV upload  
- Data preview  
- Row & column count  
- Mean, Max, Min  

---

### 🔵 Week 2 – Graph Generation

**Objective:**  
Add visualization capabilities.

**Features:**

- Plot graphs from queries  
- Numeric → Line chart  
- Categorical → Bar chart  
- Save graphs as `.png`  
- Display graphs in UI  

---

### 🟡 Week 3 – Security & Smart Queries

**Objective:**  
Improve intelligence and security.

**Features:**

- Block unsafe queries (import, exec, etc.)  
- Allow only safe operations  
- Synonyms support  
- Fuzzy column matching  
- Better error messages  

---

### 🔴 Week 4 – UI & Chat System

**Objective:**  
Enhance user experience.

**Features:**

- Chat-based interface  
- Query history  
- Sidebar with buttons  
- Auto query execution  
- Clean dashboard layout  

---

## 🌟 Bonus Features

### 🧠 Insights

- Automatic summary:
  - Mean  
  - Max  
  - Min  

### 📥 Download Report

- Export insights as `.txt` file  
- Includes dataset summary  

---

## 🧪 Example Queries

### 📊 Analysis

- mean sales  
- max quantityordered  
- sum sales  

### 📈 Graphs

- plot sales  
- plot country  
- plot productline  

### ⭐ Smart Queries

- average sales  
- total revenue  
- max price  

---

## 🔒 Security

- Blocks unsafe inputs:
  - import os  
  - exec()  
  - file operations  
- Allows only controlled queries  

---

## 🖥️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
Advanced queries (group by)

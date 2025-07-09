# 🚨 FortiGuard - AI-Based Cyber Threat Detection System

> A machine learning-powered system designed for real-time detection and counteraction of cyber threats including DDoS, DoS, MITM, and benign traffic.  
> Developed as part of an academic minor project at **SRM Institute of Science and Technology**.

---

## 📌 Overview

FortiGuard leverages supervised learning algorithms like **XGBoost** and **KNN** to analyze network traffic, identify malicious behavior, and automate mitigation.  
It integrates anomaly-based and signature-based methods for enhanced detection and real-time response.

---

## 🛠 Features

- 🔍 Detection of **DDoS**, **DoS**, **MITM**, and **Benign** traffic
- ⚙️ Real-time packet classification
- 📊 Confusion matrix, correlation heatmaps, model metrics
- 🧠 Models: XGBoost, KNN (trained on behavioral network data)
- 🚨 Autonomous mitigation logic with alert triggers
- 📈 Accuracy tuned via hyperparameter optimization

---

## 📁 Folder Structure

```text
FortiGuard-AI-Network-Threat-Detection/
├── docs/                   # Architecture, reports, review PPTs
├── src/                    # Python and notebook code
├── models/                 # Trained model files (.pkl)
├── data/                   # Dataset (if shared)
├── outputs/                # Graphs, classification reports
├── README.md
├── .gitignore
├── requirements.txt
├── LICENSE.md
```
---

## 📦 Installation

Make sure Python 3.8+ is installed.

```bash
pip install -r requirements.txt
```

If using a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Run the Project

```bash
python3 src/preprocessing_and_training.py
```

---

## 📊 Model Performance

- Metric	Value Accuracy:	~94.88%
- Classifiers:	XGBoost, KNN
- Categories:	DDoS, DoS, MITM, Benign

---

## 📚 Documentation

All supporting documents are available in the /docs folder:

- Architecture Document

- Functional Document

- Final Report

- Review Presentations (1 to 3)

- Sprint Retrospective

- Functional Test Cases

---

## 👨‍💻 Developer Info

V. Venkat Aditya
SRM Institute of Science and Technology
Reg. No.: RA2111003011799

---

## ⚠️ Disclaimer

This repository is part of academic coursework and is intended solely for educational and demonstrative purposes.

❗️Reproduction, redistribution, or commercial use of this work is strictly prohibited without explicit written permission from the author.
All rights reserved © 2024 **Venkat Aditya Vellanki**.

# 🌸 Iris Flower Classification

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![Domain](https://img.shields.io/badge/Domain-Data%20Science-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

> **CodeAlpha Data Science Internship | Project 1 of 6**

---

## 📌 Overview

A supervised machine learning project that classifies Iris flowers into three species — **Setosa**, **Versicolor**, and **Virginica** — based on their sepal and petal measurements. This project covers the complete ML pipeline from data loading to model evaluation.

---

## 🎯 Objective

Build and evaluate classification models to accurately predict Iris species from physical measurements.

---

## 📂 Project Structure

```
CodeAlpha_IrisClassification/
├── iris_classification.py       # Main ML script
├── iris_classification.ipynb    # Jupyter Notebook with full analysis
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

---

## 🧰 Tech Stack

| Library | Purpose |
|---------|---------|
| Python 3.8+ | Core language |
| Pandas | Data loading & manipulation |
| NumPy | Numerical operations |
| Matplotlib / Seaborn | Visualization |
| Scikit-learn | ML models, preprocessing, evaluation |

---

## 📊 Dataset

- **Source:** `sklearn.datasets` (UCI Iris Dataset)
- **Samples:** 150 records
- **Features:** Sepal Length, Sepal Width, Petal Length, Petal Width
- **Target:** 3 classes — Setosa, Versicolor, Virginica

---

## 🔬 Methodology

1. **Data Loading** — Load built-in Iris dataset
2. **EDA** — Statistical summaries, pair plots, correlation heatmaps
3. **Preprocessing** — Train/test split (80/20), feature scaling
4. **Modelling** — Random Forest Classifier
5. **Evaluation** — Accuracy score, Classification Report, Confusion Matrix

---

## 📈 Key Results

- Achieved high classification accuracy using Random Forest
- Clear feature importance: petal dimensions are the strongest predictors
- Confusion matrix confirms near-perfect class separation for Setosa

---

## 🚀 How to Run

```bash
# Navigate to project folder
cd CodeAlpha_IrisClassification

# Install dependencies
pip install -r requirements.txt

# Run the script
python iris_classification.py
```

---

## 📚 Key Learnings

- Supervised multi-class classification
- Feature importance analysis
- Model evaluation with confusion matrix and classification report

---

*Developed as part of the CodeAlpha Internship Program — Ameena Quadri*

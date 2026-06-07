# 📈 Sales Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![Domain](https://img.shields.io/badge/Domain-Data%20Science-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

> **CodeAlpha Data Science Internship | Project 2 of 6**

---

## 📌 Overview

A regression-based machine learning project that predicts future sales figures from advertising spend data. This project demonstrates how businesses can use predictive modelling to make data-driven marketing and budget decisions.

---

## 🎯 Objective

Predict sales performance based on advertising expenditure across different channels (TV, Radio, Newspaper) using Linear Regression.

---

## 📂 Project Structure

```
CodeAlpha_SalesPrediction/
├── sales_prediction.py          # Main ML script
├── sales_prediction.ipynb       # Jupyter Notebook with full analysis
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

---

## 🧰 Tech Stack

| Library | Purpose |
|---------|---------|
| Python 3.8+ | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Prediction visualization |
| Scikit-learn | Linear Regression, evaluation metrics |

---

## 📊 Dataset

- **Features:** TV advertising spend, Radio advertising spend, Newspaper advertising spend
- **Target:** Sales (in thousands of units)
- **Use Case:** Marketing budget optimization

---

## 🔬 Methodology

1. **Data Loading & Inspection** — Load CSV, check for nulls, review stats
2. **EDA** — Correlation analysis, scatter plots per channel
3. **Preprocessing** — Feature selection, train/test split (80/20)
4. **Modelling** — Linear Regression
5. **Evaluation** — MAE, MSE, RMSE, R² Score
6. **Visualization** — Actual vs Predicted sales plot

---

## 📈 Key Results

- Strong positive correlation between TV advertising spend and sales
- Linear Regression captures the trend effectively
- Model provides actionable insight for budget allocation

---

## 🚀 How to Run

```bash
cd CodeAlpha_SalesPrediction
pip install -r requirements.txt
python sales_prediction.py
```

---

## 📚 Key Learnings

- Regression analysis and predictive modelling
- Feature correlation and selection
- Business interpretation of ML metrics (MAE, R²)

---

*Developed as part of the CodeAlpha Internship Program — Ameena Quadri*

# Week 2 — Data Analytics with Python & AI

This week focused on **Data Analytics using Python and AI**, covering the workflow from understanding and cleaning data to exploratory analysis, statistical reasoning, and the transition from data analytics to machine learning.

## Topics Covered

### 1. Data Analytics Fundamentals
- What Data Analytics is and how an analytics project works
- The Data Analytics Lifecycle
- Four types of analytics:
  - Descriptive
  - Diagnostic
  - Predictive
  - Prescriptive

### 2. Understanding, Cleaning & Exploring Data
- Data quality and data cleaning
- Handling missing, incorrect, and duplicate data
- Exploratory Data Analysis (EDA)
- Identifying patterns, relationships, and potential data issues

### 3. Statistics, Distributions & Visualization
- Summary statistics
- Understanding data distributions
- Choosing the right chart for the data and analytical question
- Using visualization to communicate findings clearly

### 4. Correlation vs. Causation
- Understanding the difference between correlation and causation
- Why correlation alone cannot establish a causal relationship
- Common data analytics pitfalls
- The importance of questioning assumptions before drawing conclusions

### 5. From Data Analytics to Machine Learning
- Using the same data with a different type of question
- Train/Test Split
- Overfitting
- Generalization
- Data Leakage
- Understanding where AI and Machine Learning fit into the analytics workflow

> AI can speed up many stages of data analysis, but it does not remove the need to carefully check the data, assumptions, and results.

### 6. Inference with Pre-trained Models
- Introduction to inference
- Using pre-trained models to generate predictions without training a model from scratch

---

## Weekly Team Project — A/B Testing

**Team 2 Topic:**

> *What is A/B Testing, and why is it the only real way to prove causation?*

Our project explored the difference between **observational analysis and controlled experiments**.

We examined:

- Why observing more data does not necessarily prove causation
- How A/B testing compares a **Control (A)** with a **Variant (B)**
- How randomization helps reduce the influence of hidden factors
- Why companies run experiments instead of relying only on historical data
- Primary, Guardrail, and Input Metrics
- How experimental results should be interpreted before making business decisions

### Practical Case Study

We applied these concepts to an **E-Commerce Checkout** experiment.

The experiment compared an existing checkout experience with a simplified checkout flow designed to reduce friction and test whether the change improves checkout conversion.

---

## Practical Work

The week also included hands-on work using **Python and pandas** to explore, clean, analyze, and interpret data.

The A/B Testing project includes a practical `live_code.py` demonstration used to analyze experiment data and compare the Control and Treatment groups.

## Key Takeaway

**Data can tell us what happened. A well-designed experiment can help us understand what caused it.**

---

## Repository Structure

```text
week-02/
│
├── README.md
└── AB-Testing/
    ├── README.md
    ├── live_code.py
    ├── requirements.txt
    └── Figure_1.png
```

## Tools & Technologies

- Python
- pandas
- Data Analysis
- Exploratory Data Analysis (EDA)
- Statistics
- Data Visualization
- A/B Testing
- Machine Learning Fundamentals

# 🏅 Olympic Sports Recommendation System

A machine learning and sports analytics application that explores historical Olympic performance to identify patterns across countries and sports. Built with Python, Scikit-learn, and Streamlit.

## 📌 Overview

This project analyzes historical Olympic athlete and medal data to examine country-level sports performance. It combines exploratory data analysis, feature engineering, clustering, and classification in an interactive application.

## 🎯 Objectives

* Analyze Olympic participation and medal performance.
* Compare country-level performance across sports.
* Engineer features from historical Olympic data.
* Discover performance patterns using K-Means clustering.
* Use a Random Forest classifier to identify high-performing country–sport combinations.
* Present insights through an interactive Streamlit interface.

## 🛠️ Tech Stack

* **Language:** Python
* **Data Analysis:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Visualization:** Matplotlib, Seaborn (if used)
* **Application:** Streamlit
* **Development:** Jupyter Notebook / Python

## 🔍 Methodology

1. Clean and preprocess the Olympic datasets.
2. Merge athlete-event data with the NOC-to-region mapping.
3. Filter Summer Olympic events.
4. Engineer features representing country–sport participation and medal performance.
5. Apply K-Means clustering to explore performance groups.
6. Train a Random Forest classifier to predict the engineered high-performance label.
7. Evaluate the model using a train-test split.
8. Present the analysis through a Streamlit application.

## 📊 Clustering Analysis

The clustering workflow explores different country–sport performance profiles, including:

* Emerging
* Consistent
* High Performer
* Specialized

These labels describe the project's cluster interpretations and should be validated against the actual clustering results.

## 🤖 Machine Learning Model

The project uses `RandomForestClassifier` to predict a high-performance label derived from medal-rate features.

Model performance should be evaluated on held-out data. Actual accuracy and other evaluation metrics will be added after verification.

## 🖥️ Application

The Streamlit interface provides an interactive way to explore the project's Olympic sports analytics and recommendation workflow.

**Application screenshots:** To be added.

## 📁 Repository Structure

```text
Olympic-Sports-Recommendation/
├── app.py
├── README.md
├── requirements.txt
├── custom_olympic_dataset.csv
└── model.pkl
```

## ⚙️ Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/Nayan-Nayan/Olympic-Sports-Recommendation.git
cd Olympic-Sports-Recommendation
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 🚀 Future Improvements

* Add more detailed model evaluation and validation.
* Improve recommendations using additional performance features.
* Explore performance trends across Olympic editions.
* Deploy the Streamlit application online.
* Add interactive charts and country-level comparisons.

## ⚠️ Limitations

The model learns from historical Olympic data and an engineered target label. Its predictions depend on dataset coverage, feature selection, and the definition of high performance. Historical results do not guarantee future sporting success.

## 👤 Author

**Nayan**

GitHub: [@Nayan-Nayan](https://github.com/Nayan-Nayan)

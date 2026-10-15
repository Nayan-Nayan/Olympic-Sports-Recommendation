Olympic Sport Recommendation System

Overview

A machine learning project that analyzes historical Olympic athlete and medal data to explore sports performance across countries and identify high-performing country–sport combinations.

Objectives

* Analyze Olympic participation and medal performance.
* Compare country-level performance across different sports.
* Engineer meaningful features from historical Olympic data.
* Apply clustering to discover performance patterns.
* Build a classification model to identify high-performing country–sport combinations.

Dataset

The project uses the Olympic athlete events dataset and an NOC-to-region mapping dataset.

Methodology

1. Data cleaning and preprocessing
2. Merging datasets using the NOC identifier
3. Filtering Summer Olympic events
4. Feature engineering for participation and medal performance
5. K-Means clustering for exploratory segmentation
6. Random Forest classification
7. Model evaluation using a train-test split

Technologies

* Python
* Pandas
* NumPy
* Matplotlib / Seaborn (if used)
* Scikit-learn
* Jupyter Notebook

Model

The classification model uses RandomForestClassifier to predict a high-performance label derived from the medal rate.

Clusters

0 - Emerging
1 - Consistent
2 - High Performer
3 - Specialized

How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   python -m streamlit run app.py

3. Open in browser:
   http://localhost:8501


Limitations

The high-performance label is derived from historical medal rates. Predictions depend on the selected features, dataset coverage, and labeling threshold.

Future Improvements

* Evaluate the model using precision, recall, F1-score, and a confusion matrix.
* Improve the recommendation logic.
* Test generalization across different Olympic periods.
* Develop an interactive interface for exploring country–sport recommendations.
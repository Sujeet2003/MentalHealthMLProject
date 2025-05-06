### 🧠 Mental Health Depression Prediction using XGBoost
This project leverages data from the Kaggle Tabular Playground Series - November 2024 to build a predictive model for identifying individuals who may be suffering from depression, based on responses to a synthetic mental health survey.


### 📌 Project Overview
- Dataset Source: Kaggle (Tabular Playground Series - Nov 2024)
- Goal: Predict the likelihood of depression based on survey responses
- Evaluation Metric: Accuracy Score
- Model Used: XGBoost Classifier
- Tools: Python, Pandas, Seaborn, Matplotlib, Scikit-learn, XGBoost


### 🔬 Workflow
1. Data Loading
Loaded training and test datasets from the artifacts/data_ingestion/ directory.

Inspected dataset shape and types.

2. Exploratory Data Analysis (EDA)
Visualized depression distribution across:

Gender

Age

Sleep duration

Suicidal thoughts history

Plotted a heatmap of correlations between numerical features to understand relationships.

3. Data Preprocessing
Handled missing values (if any).

Encoded categorical variables as needed for model input.

Normalized/standardized numerical features for better model performance.

4. Model Development
Split data into training and validation sets.

Hyperparameter tuning using GridSearch

Trained an XGBoost Classifier, chosen for its efficiency and performance on tabular data.

Evaluated using:
    - Accuracy
    - Precision
    - Recall
    - F1 Score


### ✅ Model Performance
| Metric          | Score      |
| --------------- | ---------- |
| Accuracy Score  | 93.22% |
| Precision Score | 81.73%     |
| Recall Score    | 80.14%     |
| F1 Score        | 80.92%     |



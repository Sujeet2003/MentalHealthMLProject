### 🧠 Mental Health Depression Prediction using XGBoost
#### End-to-End Machine Learning Project

This project aims to identify individuals who may be suffering from depression using survey responses from a synthetic dataset. Built using modern MLOps practices and a modular ML pipeline, this project spans from data ingestion to model deployment. The final model is hosted live for real-time predictions:

🔗 Live App: https://mentalhealthmlproject.onrender.com

### ⚙️ Technologies Used
- Languages & Libraries: Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost
- Machine Learning: XGBoost Classifier, GridSearchCV
- Web & Visualization: Flask, HTML, CSS
- MLOps: Docker, MLflow, DVC (via Dagshub), Logging
- Experiment Tracking & Versioning: MLflow for model tracking, Dagshub for artifact and data versioning


### 📁 Project Structure

MentalHealthMLProject/
│
├── src/                            # Core ML modules
│   ├── data_ingestion/             # Load and split raw data

│   ├── data_validation/            # Schema validation & missing value checks

│   ├── data_transformation/        # Encoding, scaling, feature engineering

│   ├── model_trainer/              # Model training using XGBoost

│   ├── model_evaluation/           # Evaluation metrics & comparison

│   └── prediction/                 # Inference pipeline

│

├── templates/                      # HTML templates for web app

├── static/                         # CSS and assets

├── app.py                          # Flask application

├── Dockerfile                      # Docker container definition

├── MLproject                       # MLflow project entry point

├── requirements.txt                # Project dependencies

└── README.md                       # Project overview




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

    Visualized depression distribution across: Gender, Age, Sleep duration, Suicidal thoughts history

    Plotted a heatmap of correlations between numerical features to understand relationships.

3. Data Preprocessing

    Handled missing values.

    Encoded categorical variables as needed for model input.

    Normalized/standardized numerical features for better model performance.

4. Model Development

    Split data into training and validation sets.

    Hyperparameter tuning using GridSearch

    Trained an XGBoost Classifier, chosen for its efficiency and performance on tabular data.

    Evaluated using: Accuracy, Precision, Recall, F1 Score


### ✅ Model Performance
    | Metric          | Score      |
    | --------------- | ---------- |
    | Accuracy Score  | 93.22%     |
    | Precision Score | 81.73%     |
    | Recall Score    | 80.14%     |
    | F1 Score        | 80.92%     |

### 🖥️ Model Deployment

- Deployed via Flask Web App on Render

- Accepts user input and returns depression prediction

- HTML/CSS used for UI; hosted at:

🔗 Live Web: https://mentalhealthmlproject.onrender.com

### 🐳 How to Run with Docker
To simplify setup and ensure consistency across environments, this project is containerized using Docker.

Steps to Run the Project
- Clone the Repository
        git clone https://github.com/Sujeet2003/MentalHealthMLProject.git
  
        cd mental_health_prediction
- Build the Docker Image
        docker build -t MentalHealthMLProject .
- Run the Docker Container
        docker run -p 5000:5000 MentalHealthMLProject
- Access the App
        Open your browser and go to: http://localhost:5000



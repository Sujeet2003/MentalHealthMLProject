import os, joblib
import numpy as np
import pandas as pd
from src.MentalHealth.utils.common  import save_json
from src.MentalHealth import logger
from src.MentalHealth.config.configuration import ModelEvaluationConfig
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from pathlib import Path




class ModelEvaluation:
    def __init__(self, config=ModelEvaluationConfig):
        self.config = config

    def calculate_score(self, y_test, y_pred):
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        logger.info(f"Metrics calculated successfully with the value as: accuracy: {accuracy} & precision: {precision} & recall: {recall} & f1: {f1}")

        return accuracy, precision, recall, f1


    def evaluate_model(self) -> None:
        test_data_path = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data_path.drop(columns=['Depression'])
        y_test = test_data_path.Depression

        y_pred = model.predict(X_test)
        logger.info(f"")

        accuracy, precision, recall, f1 = self.calculate_score(y_test=y_test, y_pred=y_pred)

        scores = {
            "Accuracy Score": accuracy,
            "Precision Score": precision,
            "Recall Score": recall,
            "F1 Score": f1    
        }
        try:
            save_json(Path(self.config.metrics_file_path), scores)
            logger.info(f"Metrics file saved at: {self.config.metrics_file_path}")
        except Exception as e:
            raise Exception(e)
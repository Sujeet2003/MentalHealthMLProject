import joblib
from pathlib import Path
from src.MentalHealth import logger


class Prediction:
    def __init__(self):
        # load model
        self.model = joblib.load(Path("model.joblib"))
        logger.info(f"Model loaded for prediction stage.")
    
    def prediction(self, data: list) -> int:
        logger.info(f"Prediction initiated for the given data as: {data}")
        result = self.model.predict(data)
        logger.info(f"Prediction done for the given data for: {data} as result: {result}")
        return result

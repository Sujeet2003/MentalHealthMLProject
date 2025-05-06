import numpy as np
from src.MentalHealth.pipeline.model_prediction import Prediction


data = [1,22.0,0,2.0,5.0,0,5.0,1.0,1,1]
data = np.array(data).reshape(1, 10)
pred = Prediction()
result = pred.prediction(data=data)
print(result)
import numpy as np
from src.MentalHealth.pipeline.model_prediction import Prediction
from flask import Flask, render_template, request
from src.MentalHealth import logger
import numpy as np


# data = [1,22.0,0,2.0,5.0,0,5.0,1.0,1,1]
# data = np.array(data).reshape(1, 10)
# pred = Prediction()
# result = pred.prediction(data=data)
# print(result)
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        try:
            gender = int(request.form['gender'])
            age = float(request.form['age'])
            suicidal = int(request.form['suicidal'])
            work_hours = float(request.form['work_hours'])
            financial_stress = float(request.form['financial_stress'])
            family_history = int(request.form['family_history'])
            pressure = float(request.form['pressure'])
            satisfaction = float(request.form['satisfaction'])
            sleep_duration = int(request.form['sleep_duration'])
            dietry_habits = int(request.form['dietry_habits'])

            logger.info(f"User Data are as: Gender: {gender}, Age: {age}, Suicidal: {suicidal}, Working Hrs: {work_hours}, Financial: {financial_stress}, Family: {family_history}, Pressure: {pressure}, Satisfaction: {satisfaction}, Sleep Duration: {sleep_duration}, Diet: {dietry_habits}")

            data = [gender, age, suicidal, work_hours, financial_stress, family_history, pressure, satisfaction, sleep_duration, dietry_habits]
            data = np.array(data).reshape(1, 10)

            pred = Prediction()
            result = pred.prediction(data=data)
            logger.info(f"Prediction Done as result to: {result[0]}")

            # final_result = None
            # if result[0] == 0:
            #     final_result = "No Tension, Just Chill 😊"
            # elif result[0] == 1:
            #     final_result = "Oops, seems like you have Tension 😔."
            return render_template("index.html", result=result[0], error=None)

        except Exception as e:
            logger.info(f"Error raised during getting data from UI as: {e}")
            return render_template("index.html", result=None, error=str(e))

    return render_template("index.html", result=None, error=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
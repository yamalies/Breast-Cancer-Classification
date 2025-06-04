import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from flask import Flask
from flask import request
from flask import jsonify

app = Flask("diagnosis_breast_cancer")

# Load the trained model
model_file = "best_model.pkl"

with open(model_file, "rb") as model:
    model = pickle.load(model)

@app.route('/', methods=["GET"])
def home():
    return "Welcome to breast tumor diagnosis prediction!"

@app.route("/predict", methods=["POST"])
def predict():
    patient_values = request.get_json()

    # Transform data to 2D array
    patient_values = patient_values.values()
    data = list(patient_values)
    patient_array = np.array(data, dtype=np.float64).reshape((1, -1))

    y_pred = model.predict(patient_array)

    if y_pred == 0:
        tumor_classification = "Benign"
    else:
        tumor_classification = "Malignant"

    result = {
        "DiagnosisValue": int(y_pred),
        "TumorClassification": str(tumor_classification),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)

import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

# Load the model
model_file = "best_model.pkl"

with open(model_file, "rb") as model:
    model = pickle.load(model)

# Patient values to test
patient_values = {
    "texture_mean": 0.25160635779506246,
    "smoothness_mean": 0.2997201408323554,
    "symmetry_mean": 0.37323232323232325,
    "fractal_dimension_mean": 0.1748104465037911,
    "texture_se": 0.06789250353606789,
    "smoothness_se": 0.07393683924261481,
    "compactness_se": 0.047218133205155166,
    "concavity_se": 0.03171717171717171,
    "concave_points_se": 0.1304792574351203,
    "symmetry_se": 0.11535430854955817,
    "fractal_dimension_se": 0.02567610519187983,
    "area_worst": 0.11017990562327959,
    "smoothness_worst": 0.338968500297167,
    "symmetry_worst": 0.33609304159274594,
    "fractal_dimension_worst": 0.11976911976911982,
}

# Transform data to 2D array
patient_values = patient_values.values()
data = list(patient_values)
patient_array = np.array(data, dtype=np.float64).reshape((1, -1))

print("Tumor classification for the patient:")
print(model.predict(patient_array))

if model.predict(patient_array) == 0:
    print("The tumor is classified as benign for this patient.")

else:
    print("The tumor is classified as malignant for this patient.")

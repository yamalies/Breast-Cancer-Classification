import requests  ## to use the POST method we use a library named requests

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

# Available application URL (the containerized application is deployed here)
host = "tumor-prediction-env.eba-byntr9ky.eu-west-1.elasticbeanstalk.com"
url = f"http://{host}/predict"  ## this is the route we made for prediction

# This is the local url: uncomment it and comment the url above if you want to test the application locally
# url_local = "http://localhost:9696/predict"

response = requests.post(
    url, json=patient_values
)  ## post the customer information in json format
result = response.json()  ## get the server response
print(result)

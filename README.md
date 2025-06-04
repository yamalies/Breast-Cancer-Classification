[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Breast Cancer Malignant-Benign Classification


## Context

October is the breast cancer awareness month. 
Breast cancer is a major public health issue. It was responsible for 685000 deaths around the globe in 2020 (WHO: https://www.who.int/fr/news-room/fact-sheets/detail/breast-cancer). Half of the breast cancer cases in women appear without any risk factor other than sex and age. About 0.5-1% of breast cancers appear in men.
It is thus interesting to find new ways to detect breast cancer, especially at early stages when the disease can be treated with efficacity. We can consider tumor characteristics obtained through X-ray.

<img src="https://github.com/FoMelanie/breast_cancer_classification/blob/7408217bb4454d3b93f4d2f686cadfed85530911/data/images/breas_cancer_awareness_month.png" style="display:block;float:none;margin-left:auto;margin-right:auto;width:100%">


Starting from the Breast Cancer Dataset on Kaggle (https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset), the goal is to classify samples as:
- *Malignant*: the tumor is cancerous, which means that it grows quickly, often invade surrounding tissues and can spread to other parts of the body (metastasis)
- *Benign*: the tumor is not cancerous, which means that it grows slowly with distinct borders, it does not invade surrounding tissues and does not spread to other parts of the body


The characteristics of the tumors that are used to predict the diagnosis are physical properties such as the area of the tumor, its texture, perimeter, diameter etc... These features are explored in the exploratory data analysis part of the notebook.

## Data

The dataset can be downloaded here and is available in the data folder. Two datasets are present: the original one and a cleaned one after data cleaning (see notebook for the data preparation steps).

## Modelling

We are in a context of binary classification problem, with the two predicted classes being Benign (represented by the "0" class) and Malignant (represented by the "1" class).

All features are numerical: the most correlated ones were removed after exploratory data analysis and the remaining ones were normalized between 0 and 1.

Three models have been tested with a tuning of their hyperparameters using the scikit-learn library.

The Logistic Regression model presented the best ROC AUC metric (0.98) with the best hyperparameters and its trained version is exported to be directly used in the application.

All these steps are described in details in the ```notebook```. Please see in the sections below how to run the notebook.

## How to run the tumor diagnosis application

### Setup

Make sure to clone this repository with all files using a ```git clone``` command in the folder of your choice. 

You will need pipenv to install the dependencies from the corresponding files:

```pip install pipenv```

Then, to install the dependencies in a new environment:

```pipenv install```

You can activate your new virtual environment using:

```pipenv shell```

### Run the notebook

You can run the notebook using this command (if you are not already in the shell):

```pipenv run jupyter notebook```

Then, you just have to select the ```notebook``` notebook and run all cells. All needed files are already provided.

### Using the containerized application deployed on AWS ElasticBean

The containerized application is currently deployed on AWS ElasticBean. The application_test script takes into account the application url to make predictions: http://tumor-prediction-env.eba-byntr9ky.eu-west-1.elasticbeanstalk.com/ .

To test it, after running ```pipenv install``` , you have to run ```pipenv run python .\application_test.py``` .

The script already contains the patient values needed to get a prediction.

Here are some screens of the application predictions using AWS ElasticBean:

<img src="https://github.com/FoMelanie/breast_cancer_classification/blob/a645b0384b9d6946018834e121fb173989fe41ea/data/images/application_deployed.png" style="display:block;float:none;margin-left:auto;margin-right:auto;width:100%">

<img src="https://github.com/FoMelanie/breast_cancer_classification/blob/a645b0384b9d6946018834e121fb173989fe41ea/data/images/application_prediction.png" style="display:block;float:none;margin-left:auto;margin-right:auto;width:100%">

### How to deploy to cloud

In order to deploy the containerized application to the cloud by yourself, you must follow these steps:

1 - Create a AWS account

2 - Configure a user account with the right permissions (root user IAM setup) to create a AWS EB environment

3 - Run the following command to init the EB environment:

```eb init -p "Docker running on 64bit Amazon Linux 2" tumor-diagnosis-serving -r eu-west-1```

 You will have to change the location based on your own location.

 4 - Finally, create the environment application by running this command:

 ```eb create tumor-prediction-env```

 5 - When the application is running, you can test it directly by running:

 ```pipenv run python .\application_test.py```

### Locally without Docker


If you are on Windows, you can run the application in production environment with this command:

```pipenv run gunicorn --bind 0.0.0.0:9696 application:app```

If you are not working on Windows, you can run the application in production environment with this command:

```pipenv run waitress-serve --listen=0.0.0.0:9696 application:app```

You can test the application prediction with the test python script ```application_test.py``` with this command:

```pipenv run python application_test.py```

The output should be a DiagnosisValue equal to 0 and TumorClassification equal to "Benign".

*Note*: You can also run the application locally with debug mode on with this command line:

```pipenv run python application.py```


### Locally with Docker

First, make sure that Docker Desktop is running on your computer.
Using the provided Dockerfile, build the Docker container with this command:

```docker build -t tumor-diagnosis-prediction .```

Run the Docker container:

```docker run -it -p 9696:9696 tumor-diagnosis-prediction:latest```

Finally, you can test that the containerized application correctly works using this command:

```pipenv run python application.py```

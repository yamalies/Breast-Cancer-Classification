from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle


# --- Cleaned dataset loading
data = pd.read_csv("data/clean_breast_cancer_dataset.csv")

# --- Split into train, val, test datasets

# First generate the full training dataset and the test dataset
full_train, test = train_test_split(data, test_size=0.2, random_state=42)

# Then separate the full training dataset into train and validation datasets. We have to adjust the proportions:
# we need 20% of the total number of rows from the 80% of values, which means we are looking for 0.25 proportion for the validation dataset
train, val = train_test_split(full_train, test_size=0.25, random_state=42)

# Select the target values (here "diagnosis") from original datasets
y_train = train["diagnosis"]
y_val = val["diagnosis"]
y_test = test["diagnosis"]

# Remove the target column (here "diagnosis") from features dataset
del train["diagnosis"]
del val["diagnosis"]
del test["diagnosis"]

# --- Train the model
model = LogisticRegression(C=10, penalty="l1", solver="liblinear")
model.fit(train, y_train)

# --- Export trained model
pickle.dump(model, open("best_model.pkl", "wb"))

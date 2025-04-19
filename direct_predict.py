"""
Script to directly load the trained model from MLflow and make predictions.
This bypasses the need for a running prediction service.
"""
import os
import pandas as pd
import mlflow
from mlflow.tracking import MlflowClient

# Set the MLflow tracking URI to the local mlruns directory
mlflow.set_tracking_uri(f"file://{os.path.abspath('mlruns')}")

# Create a client
client = MlflowClient()

# Get the latest run ID from experiment 0
runs = client.search_runs(experiment_ids=["0"], order_by=["start_time DESC"], max_results=1)
if not runs:
    print("No runs found in the MLflow tracking server.")
    exit(1)

latest_run = runs[0]
run_id = latest_run.info.run_id
print(f"Using model from run: {run_id}")

# Load the model
model_uri = f"runs:/{run_id}/model"
try:
    model = mlflow.pyfunc.load_model(model_uri)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

# Sample input data for prediction (same as in sample_predict.py)
input_data = pd.DataFrame([{
    "Order": 1,
    "PID": 5286,
    "MS SubClass": 20,
    "Lot Frontage": 80.0,
    "Lot Area": 9600,
    "Overall Qual": 5,
    "Overall Cond": 7,
    "Year Built": 1961,
    "Year Remod/Add": 1961,
    "Mas Vnr Area": 0.0,
    "BsmtFin SF 1": 700.0,
    "BsmtFin SF 2": 0.0,
    "Bsmt Unf SF": 150.0,
    "Total Bsmt SF": 850.0,
    "1st Flr SF": 856,
    "2nd Flr SF": 854,
    "Low Qual Fin SF": 0,
    "Gr Liv Area": 1710.0,
    "Bsmt Full Bath": 1,
    "Bsmt Half Bath": 0,
    "Full Bath": 1,
    "Half Bath": 0,
    "Bedroom AbvGr": 3,
    "Kitchen AbvGr": 1,
    "TotRms AbvGrd": 7,
    "Fireplaces": 2,
    "Garage Yr Blt": 1961,
    "Garage Cars": 2,
    "Garage Area": 500.0,
    "Wood Deck SF": 210.0,
    "Open Porch SF": 0,
    "Enclosed Porch": 0,
    "3Ssn Porch": 0,
    "Screen Porch": 0,
    "Pool Area": 0,
    "Misc Val": 0,
    "Mo Sold": 5,
    "Yr Sold": 2010,
}])

# Make prediction
try:
    prediction = model.predict(input_data)
    print("\nPrediction result:")
    print(f"Predicted house price: ${prediction[0]:.2f}")
except Exception as e:
    print(f"Error making prediction: {e}")
    
    # Print more details about the model's expected input
    print("\nModel input schema:")
    if hasattr(model, 'metadata') and hasattr(model.metadata, 'signature'):
        print(model.metadata.signature)
    else:
        print("Model signature not available")
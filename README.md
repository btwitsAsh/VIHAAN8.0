# VIHAAN8.0
# 🏡 Smart House Price Predictor with MLOps Integration

An end-to-end machine learning project that transforms raw real estate data into intelligent, explainable, and production-ready house price predictions using scalable ML engineering and MLOps best practices.

---

## 📌 Problem Statement

Accurate house price prediction is a critical challenge in the real estate industry. Traditional valuation methods are often manual, inconsistent, and lack transparency. With real estate prices influenced by a wide range of factors—location, area, amenities, and market trends—there's a pressing need for a robust, data-driven solution that can:

- Predict property prices accurately
- Explain the factors influencing the price
- Be maintained, monitored, and scaled with new data

This project solves that by combining machine learning with MLOps tools like **ZenML** and **MLflow** to deliver a complete, production-ready pipeline.

---

## 🛠️ Approach

We followed a modular and scalable ML development process:

### 🔄 Pipeline Stages:

1. **Data Collection & Preprocessing**
   - Load structured housing data (CSV format)
   - Handle nulls, outliers, and incorrect data types

2. **Exploratory Data Analysis (EDA)**
   - Analyze trends, distributions, correlations
   - Visualize feature relationships using Seaborn & Plotly

3. **Feature Engineering**
   - Create domain-relevant features (e.g., age of house, price per sqft)
   - One-hot encode categoricals, normalize numerical data

4. **Model Building**
   - Use XGBoost/RandomForest for regression
   - Tune hyperparameters using cross-validation
   - Evaluate using MAE, RMSE, R2

5. **Experiment Tracking with MLflow**
   - Log metrics, parameters, artifacts
   - Track and compare model runs

6. **Pipeline Orchestration with ZenML**
   - Build modular pipelines (data ingestion, training, evaluation)
   - Automate reproducible workflows

7. **Model Deployment**
   - Serve model with FastAPI
   - Dockerize the service for scalability

---

## 🌟 Unique Value Proposition

### ✅ MLOps-Integrated Workflow
- Full ML lifecycle: data → model → deployment
- ZenML handles orchestration; MLflow handles logging

### ✅ Reproducibility & Scalability
- Modular codebase using design patterns
- Pipeline components are version-controlled and reusable

### ✅ Explainability
- SHAP values and feature importances for model transparency

### ✅ Deployable
- FastAPI for RESTful prediction API
- Dockerized app ready for deployment to cloud platforms (AWS/GCP/Azure)

---

## 🔧 Tech Stack

- **Languages & Libraries:** Python, Pandas, NumPy, scikit-learn, XGBoost, Matplotlib, SHAP
- **MLOps Tools:** ZenML, MLflow
- **Deployment:** FastAPI, Docker
- **Visualization:** Seaborn, Plotly, SHAP

---

## 🖼️ Architecture Diagram

```
[Data Ingestion] → [EDA & Feature Engineering] → [Model Training] → [Evaluation] → [MLflow Tracking]
      ↓
 [ZenML Pipelines] → [FastAPI Serving] → [Docker Container] → [Deployment]
```

---

## 🚀 How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/smart-house-price-predictor.git
cd smart-house-price-predictor
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run ZenML Pipeline
```bash
zenml init
python run_pipeline.py
```

### 4. Launch MLflow UI
```bash
mlflow ui
# visit http://localhost:5000
```

### 5. Run FastAPI Server
```bash
uvicorn api.main:app --reload
# visit http://localhost:8000/docs
```

### 6. Dockerize (Optional)
```bash
docker build -t house-price-api .
docker run -p 8000:8000 house-price-api
```

---

## 📊 Results

| Metric | Value |
|--------|--------|
| MAE    | 12,000 |
| RMSE   | 18,500 |
| R²     | 0.92   |

Includes SHAP visualizations, residual plots, and model comparison in MLflow.

---

## 📈 Future Work

- Add real-time data ingestion
- Implement active learning feedback loop
- Build Streamlit dashboard for UI
- Deploy to AWS Lambda with CI/CD




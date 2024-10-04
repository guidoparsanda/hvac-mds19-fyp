# hvac-energy-optimization
MDS19-MONASH2024-Main Repository to organize files

# HVAC Energy Optimization Project

## Overview

This project aims to build a web-based system that predicts energy consumption and provides recommendations using machine learning models. We've trained a Voting Regressor model (consisting of Gradient Boosting, Decision Tree, and Random Forest) and integrated it with a FastAPI backend to handle energy data submissions and generate recommendations.

## What to Do Next

### 1. **Setting Up the Environment**
   - Ensure you have all the required dependencies installed:
     - FastAPI for the backend
     - Pydantic for data validation
     - Pandas, Numpy for data handling
     - Scikit-learn for machine learning models
     - joblib for model serialization/deserialization
   - Run `pip install -r requirements.txt` if we have the requirements file, or install manually if necessary.

### 2. **Running the Web App**
   - Ensure `main.py` is working locally.
   - The web app is designed to be used locally for demo purposes, so you do not need to host it on the cloud or a server.
   - Run `uvicorn main:app --reload` to start the FastAPI server on your machine.

### 3. **Simulating Energy Data**
   - You don't need to rely on user input; we will showcase the app with simulated data for the demo. Prepare some simulated data for energy consumption predictions (temperature, humidity, etc.) in advance.

### 4. **Integrating with the Frontend**
   - The frontend is developed in React (check the `hvac_dashboard` folder).
   - You can send POST requests to `/submit/` for submitting energy data, and GET requests to `/recommendations/` for retrieving model-based recommendations.

## What to Avoid

- **Do NOT retrain the model** unless necessary. We've saved the trained model in `voting_regressor_with_rf.pkl`. Re-training would take a long time and should only be done if absolutely required.
- **Do NOT push unnecessary files** to GitHub (e.g., large datasets, `.pkl` models). Stick to pushing code and small files unless specifically required.
- **Do NOT modify the core machine learning pipeline** without understanding its impact. Discuss with the team before making changes to `model.ipynb` or `hvac_ml_model.py`.

## Warnings & Watch-Outs

1. **Model Integration**:
   - We are using serialized models (`.pkl` format) to avoid retraining. Ensure that the model file is accessible and not modified accidentally.
   
2. **FastAPI Issues**:
   - Ensure all the imports and libraries are compatible with the version. If there are issues with certain dependencies, use the versions specified in the `requirements.txt`.
   
3. **Simulated Data**:
   - When preparing for the demo, please ensure that the simulated data used for POST requests is realistic. 

Coordinate with the front-end team to ensure consistency, and always keep each other posted on progress ya!

## Remaining Tasks
   - Complete frontend/backend integration (local only).
   - Test the whole workflow (submitting energy data, getting recommendations).
   - Coordinate with other teams to ensure the dashboard looks and feels professional for demo day.

## For Demo Day
   - The web app is designed to be showcased using **localhost** or local commands.
   - Ensure all APIs are functioning, and you have tested the system with demo data.

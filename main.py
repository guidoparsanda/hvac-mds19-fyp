# main.py
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer
import joblib
import numpy as np
import logging

# Setup basic logging ( can replace with more advanced logging later )
logging.basicConfig(level=logging.INFO)

# Load the saved machine learning model (already saved, just load it)
voting_regressor = joblib.load('voting_regressor_with_rf.pkl')

app = FastAPI()

# OAuth2 placeholder for login (authentication to be added later)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# BaseModel for energy data submission
class EnergyData(BaseModel):
    temperature: float
    humidity: float
    occupancy: int
    timestamp: str

# Basic login route (to be enhanced later)
# Dont forget to replace the token with the actual token later and enhance the login logic ya!
@app.post("/login/")
async def login(token: str = Depends(oauth2_scheme)):
    if token == "test-token":  # Placeholder for authentication logic
        return {"message": "Login successful!"}
    raise HTTPException(status_code=400, detail="Invalid credentials")

# Energy data submission route
@app.post("/submit/")
async def submit_energy_data(data: EnergyData, background_tasks: BackgroundTasks):
    try:
        # Simulating saving the energy data (this would be connected to a database)
        background_tasks.add_task(log_energy_data, data)
        return {"message": "Energy data submitted successfully!", "data": data}
    except Exception as e:
        logging.error(f"Error submitting data: {e}")
        raise HTTPException(status_code=500, detail="Failed to submit data")

def log_energy_data(data: EnergyData):
    # Function to log or process energy data in the background (placeholder)
    logging.info(f"Energy data received: {data}")

# Route for generating ML-based energy optimization recommendations
@app.post("/recommendations/")
async def get_recommendations(data: EnergyData):
    try:
        # Prepare the input for the model (using the simulated data for now)
        model_input = np.array([[data.temperature, data.humidity, data.occupancy]])
        prediction = voting_regressor.predict(model_input)
        return {
            "message": "Recommendation generated!",
            "predicted_meter_reading": prediction[0]
        }
    except Exception as e:
        logging.error(f"Error generating recommendation: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate recommendation")

# Error handling example for invalid routes
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    return {
        "message": "An error occurred",
        "details": exc.detail
    }

# Example of a route to showcase demo mode ( please replace if needed guys )
@app.get("/demo/")
async def demo_mode():
    # This route will provide a message showcasing the demo mode ( can replace later )
    return {"message": "USER demo mode running. Pre-simulated data is being used for all predictions."}
# Crop Prediction API

This is a FastAPI-based REST API that predicts the best crop to grow based on soil and environmental parameters. It takes inputs such as Nitrogen, Phosphorous, Potassium content, temperature, humidity, pH, and rainfall, then returns a crop recommendation using a trained machine learning model.

---

## Features

- REST API with `/predict` endpoint for crop recommendation
- Input validation using Pydantic models with detailed schema
- Uses a preprocessing scaler (`ssc`) and trained model (`lr`) for prediction
- Returns JSON response with predicted crop

---

## Tech Stack

- Python 3.x
- [FastAPI](https://fastapi.tiangolo.com/) for API framework
- [Pydantic](https://pydantic.dev/) for data validation and parsing
- Machine learning model 
- Pandas for data handling


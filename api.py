from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.input_schema import crop_parameter
import pandas as pd
from models.models import ssc,lr

app=FastAPI()

@app.get("/")
def welcome():
    return {"message":"Welcome to crop prediction api"}

@app.post("/predict")
def predict(crop_param:crop_parameter):
    input_data={
        "N":crop_param.n,
        "P":crop_param.p,
        "K":crop_param.k,
        "temperature":crop_param.temp,
        "humidity":crop_param.humidity,
        "ph":crop_param.ph,
        "rainfall":crop_param.rainfall
    }
    input_data=pd.DataFrame([input_data])
    scaled_data=ssc.transform(input_data)
    prediction=lr.predict(scaled_data)
    return {"prediction":prediction[0]}



from pydantic import BaseModel,Field
from typing import Annotated

class crop_parameter(BaseModel):
    n:Annotated[int,Field(...,title="Nitrogen Content",description="Enter the percentage of nitrogen in soil",gt=0,lt=100,examples=["50","60","70"])]
    p:Annotated[int,Field(...,title="phosphorous Content",description="Enter the percentage of phosphorous in soil",gt=0,lt=100,examples=["50","60","70"])]
    k:Annotated[int,Field(...,title="potassium Content",description="Enter the percentage of potassium in soil",gt=0,lt=100,examples=["50","60","70"])]
    temp:Annotated[float,Field(...,title="Temperature",description="Enter the temperature of farm environment in degree celsius",gt=0,lt=60,examples=["20.978","19.977","30.76"])]
    humidity:Annotated[float,Field(...,title="Humidity",description="Enter the Humidity of farm environment in percent",gt=0,lt=100,examples=["82.00274423","80.15836264"])]
    ph:Annotated[float,Field(...,title="Ph",description="Enter the Ph of farm environment",gt=0,lt=14,examples=["6.3434","4.2439"])]
    rainfall:Annotated[float,Field(...,title="rainfall",description="Enter the rainfall in cm",gt=0,lt=100,examples=["82.00274423","80.15836264"])]


import pandas as pd
import numpy as np
from typing import Optional 
from fastapi import FastAPI,Path
from pydantic import BaseModel
from pydantic import Field
from typing import Literal
from preprocessing import cleaning_data as cl
from predict import prediction

# class Item(BaseModel):

#     salary:int
#     bonus: int
#     taxes: int


# class Properties(BaseModel):
#     zip_code: int
#     full_address: Optional[str]
['Zip code', 'Type of Property', 'Subtype of Property', 'Price (€)',
       'Bedrooms', 'Living area (m²)', 'Kitchen type', 'How many fireplaces?',
       'Terrace', 'Terrace surface (m²)', 'Garden', 'Garden surface (m²)',
       'Surface of the plot (m²)', 'Number of frontages', 'Swimming pool',
       'Building condition', 'Basement', 'Energy class', 'Heating type',
       'Kitchen type scale', 'Building condition scale', 'Region']
    
class Property(BaseModel):
    Property_type: Literal['apartment','house'] = Field(description="Only 'Appartment' and 'House' fields are available")
    Property_sub_type: Literal['duplex', 'penthouse', 'flat studio', 'mansion', 'villa',
       'apartment block', 'town house', 'loft', 'house', 'apartment',
       'exceptional property', 'country cottage', 'triplex', 'bungalow',
       'ground floor', 'chalet', 'mixed use building', 'castle',
       'service flat', 'manor house', 'farmhouse', 'other property',
       'kot'] = Field(description = "The condition of the building ")
    Bed_rooms: int = Field(gt=1,lt=50, description="At least one bed room and maximum 50")
    Living_area: int = Field(gt=10, description="At least a house with 10 square meters living area")
    Kitchen_type: Literal['USA hyper equipped', 'Installed', 'Hyper equipped',
       'USA installed','Semi equipped', 'USA semi equipped',
       'Not installed', 'USA uninstalled'] | None = Field(default = "Empty",description = "Enter 1 if there is a Terrace ")
    Fire_place: int | None = Field(default = 0,description = "Enter 1 if there is a fireplace and 1 if there are none")
    Terrace: int | None = Field(default = 0,description = "Enter 1 if there is a Terrace ")
    Terrace_surface: int | None = Field(default = 0,description= " The surface of the Terrace in square meters")
    Garden: int | None = Field(default = 0,description = "Enter 1 if you have a Garden ")
    Garden_surface: int | None = Field(default = 0,description= " The surface of the Garden in square meters")
    Surface_of_plot: int | None = Field(default = 0, gt=10,description=" Enter the Surface of the plot in Square meters")
    facades_number:int | None = Field(default = 0,description= " The number of facade")
    Swimming_pool:int | None = Field(default = 0,description= " Enter 1 if you have a swimming pool ")
    Building_condition: Literal['As new', 'Good', 'Just renovated', 'To be done up', 'To renovate','To restore'] | None = Field(default = "Empty",description = "The condition of the building ")
    Basement:int | None = Field(default = 0,description= " Enter 1 if you have a Basement")
    Energy_class:Literal['B', 'F', 'E', 'G', 'C', 'D', 'A', 'A++', 'A+', 'A_A+',
       'G_A++', 'G_F', 'E_D', 'C_B', 'D_C', 'E_C', 'G_C', 'F_B'] | None = Field(default = "Empty",description = " The energy class Entry")
    Heating_type:Literal['Gas', 'Electric', 'Fuel oil', 'Pellet', 'Wood', 'Solar',
       'Carbon'] | None = Field(default = "Empty",description="The Heating type Entry ")
    Region:Literal ['Walloon', 'Brussels capital region', 'Flander'] | None = Field(default = "Empty", description="Select the Region ")
    
    

# class prediction(BaseModel):  
#   prediction: Optional[float]

app = FastAPI()

# @app.get("/path/{number}")
# async def Mult_num(number: int = Path(description='Enter the number to multiply by 2')):
#     return number * 2

# @app.post("/items/")
# async def create_item(item: Item):
#     return item.salary + item.bonus - item.taxes


@app.post("/items/")
async def create_item(prop: Property):
    df_processed = cl.preprocess(prop)
    pred = prediction.predict(df_processed)
    return f"{pred}"


# @app.post("/prediction/")
# async def prediction(data):
#     return data


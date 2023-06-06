import pandas as pd
from typing import Optional 
from fastapi import FastAPI,Path
from pydantic import BaseModel
from pydantic import Field
from typing import Literal



# class Item(BaseModel):

#     salary:int
#     bonus: int
#     taxes: int


# class Properties(BaseModel):
#     area: int
#     property_type: str
#     rooms_number: int
#     zip_code: int
#     land_area: Optional[int]
#     garden: Optional[bool]
#     garden_area: Optional[int]
#     equipped_kitchen: Optional[bool]
#     full_address: Optional[str]
#     swimming_pool: Optional[bool]
#     furnished: Optional[bool]
#     open_fire: Optional[bool]
#     terrace: Optional[bool]
#     terrace_area: Optional[int]
#     facades_number: Optional[int]
#     building_state: Optional[str]
    
class Property(BaseModel):
    Property_type: Literal['appartment','house'] = Field(description="Only 'Appartment' and 'House' fields are available")
    Bed_rooms: int = Field(gt=1,lt=50, description="At least one bed room and maximum 50")
    Living_area: int = Field(gt=10, description="At least a house with 10 square meters living area")
    Fire_place: int | None = Field(default = 0,description = "Enter 1 if there is a fireplace and 1 if there are none")
    Terrace: int | None = Field(default = 0,description = "Enter 1 if there is a Terrace ")
    Terrace_surface: int | None = Field(default = 0,description= " The surface of the Terrace in square meters")
    Garden: int | None = Field(default = 0,description = "Enter 1 if you have a Garden ")
    Garden_surface: int | None = Field(default = 0,description= " The surface of the Garden in square meters")
    Frontages:int | None = Field(default = 0,description= " The number of facade")
    Swimming_pool:int | None = Field(default = 0,description= " Enter 1 if you have a swimming pool ")
    Basement:int | None = Field(default = 0,description= " Enter 1 if you have a Basement")
    Kitchen_type: Literal['USA hyper equipped', 'Installed', 'Hyper equipped',
       'USA installed','Semi equipped', 'USA semi equipped',
       'Not installed', 'USA uninstalled'] | None = Field(default = 0,description = "Enter 1 if there is a Terrace ")
    Building_condition: Literal['As new', 'Good', 'Just renovated', 'To be done up', 'To renovate',
                                'To restore'] | None = Field(default = 0,description = "The condition of the building ")
    Property_sub_type: Literal['duplex', 'penthouse', 'flat studio', 'mansion', 'villa',
       'apartment block', 'town house', 'loft', 'house', 'apartment',
       'exceptional property', 'country cottage', 'triplex', 'bungalow',
       'ground floor', 'chalet', 'mixed use building', 'castle',
       'service flat', 'manor house', 'farmhouse', 'other property',
       'kot'] | None = Field(default = 0,description = "The condition of the building ")
    Energy_class:Literal['B', 'F', 'E', 'G', 'C', 'D', 'A', 'A++', 'A+', 'A_A+',
       'G_A++', 'G_F', 'E_D', 'C_B', 'D_C', 'E_C', 'G_C', 'F_B'] | None = Field(default = 0,description = " The energy class Entry")
    Heating_type:Literal['Gas', 'Electric', 'Fuel oil', 'Pellet', 'Wood', 'Solar',
       'Carbon'] | None = Field(default = 0,description="The Heating type Entry ")
    Region:Literal ['Walloon', 'Brussels capital region', 'Flemish'] | None = Field(default = 0, description="Select the Region ")
    


building_condition_scale={'As new':6,'Just renovated':5, 'Good':4, 'To renovate':2,
'To restore':1, 'To be done up':3}



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
    return f"""the house type is {prop.Property_type}
    bed rooms are {prop.Bed_rooms}
    Living_area is {prop.Living_area}

    {prop.Fire_place}
    {prop.Terrace}
    {prop.Terrace_surface} 
    {prop.Garden }
    {prop.Garden_surface} 
    {prop.Frontages }
    {prop.Swimming_pool} 
    {prop.Basement} 
    {prop.Kitchen_type} 
    {prop.Building_condition} 
    {prop.Property_sub_type} 
    {prop.Energy_class} 
    {prop.Heating_type} 
    {prop.Region}
    """


# @app.post("/prediction/")
# async def prediction(data):
#     return data


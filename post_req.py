from fastapi import FastAPI, HTTPException
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, List, Literal

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="This is the id section of the patient", examples=["P001", "P004"])]
    name: Annotated[str, Field(max_length=50, description="The max length of the field could be 50 letters only", examples=["Taran Pal Singh, Zakir Khan"])]
    city: str
    age: Annotated[int, Field(ge=0, le=150, description="The range is 0-150", examples=['20', '100', '150'])]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description="This is the gender section of the patient class")]
    height: Annotated[float, Field(..., description="This is the height class of the patient object", ge=0)]
    weight: Annotated[float, Field(..., description="This is the weight class of the patient object", ge=0)]


    @computed_field()
    @property

    def bmi(self)->float:
        bmi = self.weight/self.height**2
        return bmi
    

    @computed_field
    @property
    def condition(self)->str:
        if 18.5 < self.bmi < 24.9:
            return "healthy"
        
        if self.bmi<18.5:
            return "underweight"
        
        if self.bmi>24.9:
            return "obese"


app=FastAPI()   

def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open ("patients.json", "w") as f:
        data= json.dump(data, f)
       

        
    
@app.get('/view')
def get_viewers():
    return [load_data()]

@app.post('/create')
def create_patient(object: Patient):
    #load the data
    data = load_data()
    #check if the patient already exists or not
    if object.id in data:
        return HTTPException(status_code=400, detail="The patient already exists")
    # if not then insert into the database
    data[object.id] = object.model_dump(exclude=['id'])
    save_data(data)

    JSONResponse(status_code=201, content={"message":"Patient Created Successfully"})








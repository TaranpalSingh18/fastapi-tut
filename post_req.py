from fastapi import FastAPI, HTTPException
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
app=FastAPI()   

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="This is the id section of the patient", examples=["P001", "P004"])]
    name: Annotated[str, Field(max_length=50, description="The max length of the field could be 50 letters only", examples=["Taran Pal Singh, Zakir Khan"])]
    city: str
    age: Annotated[int, Field(ge=0, le=150, description="The range is 0-150", examples=['20', '100', '150'])]
    gender: Annotated[Literal['male', 'female', 'others'], Field(description="This is the gender section of the patient class")]
    height: Annotated[float, Field( description="This is the height class of the patient object", ge=0)]
    weight: Annotated[float, Field( description="This is the weight class of the patient object", ge=0)]

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
        
def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open ("patients.json", "w") as f:
        data= json.dump(data, f)
       

class Patient_update(BaseModel):
    id: Annotated[Optional[str], Field(default=None)]
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None)]
    gender: Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None)]
    height: Annotated[Optional[float], Field(description="This is the height class of the patient object", ge=0, default=None)]
    weight: Annotated[Optional[float], Field(description="This is the weight class of the patient object", ge=0, default=None)]   
    
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

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, object: Patient_update):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="The following patient id is not found")
    
    existing_patient_data = data[patient_id]
    new_patient_data = object.model_dump(exclude_unset=True)

    for key,value in new_patient_data.items():
        existing_patient_data[key]=value

    existing_patient_data['id']=patient_id

    validated_patient_updated_data= Patient(**existing_patient_data)
    #pydantic object into dictionary
    updated_data = validated_patient_updated_data.model_dump(exclude='id')

    data[patient_id]=updated_data
    
    save_data(data)

    return JSONResponse(status_code=200, content="Successfully updated teh data")

@app.delete('/delete/{patient_id}')
def delete_patient(patiend_id:str):
    data = load_data()
    if patiend_id not in data:
        raise HTTPException(status_code=404, detail="patient not found")
    
    del data[patiend_id]
    save_data(data)

    return JSONResponse(status_code=200, content="Patient deleted")




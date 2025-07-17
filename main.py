from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data
 

@app.get("/")
def read_root():
    return {"message: This is a patient management api"}

@app.get('/about')
def about():
    return {"We are learning fastAPI from basics"}


@app.get('/view')
def view_files():
    return {"message":load_data()}

@app.get('/view/{patient_id}')
def get_patient(patient_id: str):
    data = load_data()
    if patient_id in data:
        return  {patient_id:data[patient_id]}
    raise HTTPException(status_code=404, detail="The patient ID is not found")

from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age: int

def patient_name(patient: Patient):
    print(patient.name)
    print(patient.age)    

patient={"name":"Taran Pal Singh", "age":"30"}

patient1=Patient(**patient)

patient_name(patient1)

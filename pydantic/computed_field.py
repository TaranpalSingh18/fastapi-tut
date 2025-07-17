from pydantic import BaseModel, computed_field

class Patient(BaseModel):
    name: str
    age:int
    height: float
    weight: float

    @computed_field
    @property
    def bmi(self)-> float:
        bmi=self.weight/self.height**2
        return bmi
    
def patient_function(patient_object: Patient):
    print({"BMI IS":patient_object.bmi})

patient_one={"name":"Taran", "age":20, "height":1.72, "weight":72.3}

validate_patient_one= Patient(**patient_one)
patient_function(validate_patient_one)


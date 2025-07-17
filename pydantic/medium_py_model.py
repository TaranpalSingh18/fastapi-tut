from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Dict, List, Optional

class Patient(BaseModel):
    name: str= Field(max_length=10)
    email_id: EmailStr
    linkedin_url: Optional[AnyUrl]="http\\linkedin123.in"
    age: int = Field(gt=0 ,lt=90)
    married: bool
    contact_details: Dict[str, str]
    symptoms:List[str]
    gender:Optional[str]=None
    #by default value remains None

def patient_function(obj: Patient):
    for i in obj.symptoms:
        print(i)
    for i in obj.contact_details:
        print(obj.contact_details[i])
    print(obj.gender)
    print(obj.email_id)
    print(obj.linkedin_url)

patient_object = {"name":"TaranPalSingh", "email_id":"taran23100@iiitnr.edu.in","age":20,"married":False, "contact_details":{"Taran Pal Singh": "+91 7470369221"}, "symptoms":["Cough", "Cold", "Fever"], "gender": "Male"}

validated_object = Patient(**patient_object)

patient_function(validated_object)

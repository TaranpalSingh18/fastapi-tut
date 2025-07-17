from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import Annotated, Dict, List, Optional

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, description="This is a name field", examples=["Taran", "Amit", "Manreet"])]
    email: EmailStr 
    age: Annotated[int, Field(gt=0, lt=100)]
    isMarried: Annotated[bool, Field(default=False)]
    linkedin_url: AnyUrl
    contact_details: Dict[str, str]
    allergies: Annotated[Optional[List[str]], Field(max_length=4)]

store_allergies=[]

def patient_function (object: Patient):
    print(object.name)
    for i in object.allergies:
        store_allergies.append(i)
    
    for j in object.contact_details:
        print({j: object.contact_details[j]})


patient_object ={"name": "Taran Pal Singh","email":"taran23100@gmail.com", "age":"20","linkedin_url":"https://www.linkedin.com/in/taran-pal-singh-75b58927a/", "contact_details":{"JP Singh":"+91 9015537221"}, "allergies":["Allergy from Dust", "Allergy from Milk"]}

validated_object = Patient(**patient_object)

patient_function(validated_object)

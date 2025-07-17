from pydantic import BaseModel, EmailStr, AnyUrl,  field_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age:int
    email:EmailStr
    linkedin_url: AnyUrl
    contact_details: Dict[str, str] # {}

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains=['hdfc.com','icic.com', 'walmart.in']
        splitted_text = value.split('@')[-1]

        if splitted_text not in valid_domains:
            return ValueError({"Not in specified domains"})
        else:
            return value
        

    @field_validator('name')
    @classmethod
    def first_index_upper(cls, value):
        n = value[0].upper()
        m = value.split(value[0])[-1]
        return n+m
    
    @field_validator('age', mode="before")
    @classmethod

    def validate_age(cls, value):
        if value> 0 and value <100:
            return value
        
        else:
            return ValueError("The age is beyond or below the age limit")
        
    @field_validator('contact_details')
    @classmethod

    def emergency_contact(cls, value):
        if 'emergency' not in value:
            return ValueError("No Emergency Field Present")
        
        else:
            return value
        
        
    
def patient_function(object: Patient):
    print(object.name)
    print(object.email)
    print(object.age)

patient_object={"name":"taran", "age":"59", "email":"taran@hdfc.com", "linkedin_url":"https://www.linkedin.com/in/arshkhatwani/","contact_details":{"JP Singh":"+91 9015537221"}}

validated_object = Patient(**patient_object)
patient_function(validated_object)

""""
field_validator has two modes: mainly before and after 
by default it runs on after mode: that is runs after type coersion of python
(simple shabdo mei: jab hum bolte hai ki ki pydantic smart hai..agar class mei age int mei mentioned hai, lekin aap str ke form mei pass kr rhe ho toh, toh pydantic type coersion ke through usko apne aap convert kr leta hai)

(but agar aapki field_validator ka mode=="before" hai toh pehle aapka validator chalega fir type coersion hoga...yaani agar aapki age int mei defined hai and aapne str pe pass kri hui hai toh value error aayega.)
"""


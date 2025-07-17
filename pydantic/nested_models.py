from pydantic import BaseModel
from typing import List, Dict


class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name: str
    age: int
    height: float
    address: Address

address_obj={"city":"Raipur","state":"Chhattisgarh", "pincode":23100055}
validated_address=Address(**address_obj)
print
patient_obj={"name":"Taran Pal Singh", "age":20, "height":1.84, "address":validated_address}
validated_patient_obj=Patient(**patient_obj)

print(validated_patient_obj.address.city)
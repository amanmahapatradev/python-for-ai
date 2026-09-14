from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict

class PatientData(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_info: Dict[str, str]

    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["gmail.com", "hdfc.com", "icici.com"]

        domain_name = str(value).split("@")[-1].lower()

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")

        return value


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_info)


patient_data = {
    "name": "John",
    "email": "john1458@gmail.com",
    "age": 25,
    "weight": 51.25,
    "married": True,
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {
        "phone": "354-168-2458"
    }
}

patient_1 = PatientData(**patient_data)

add_patient_data(patient_1)
from typing import List
from pydantic import BaseModel


class PatientData(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_info: dict[str, str]


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully\n")


def update_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print("Data updated successfully\n")


# Patient 1
patient_data_1 = {
    "name": "John",
    "age": 25,
    "weight": 51.25,
    "married": True,
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {
        "email": "john5366@gmail.com",
        "phone": "354-168-2458",
    },
}

patient_1 = PatientData(**patient_data_1)


# Patient 2
patient_data_2 = {
    "name": "Alex",
    "age": 45,
    "weight": 67.25,
    "married": False,
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {
        "email": "alex366@gmail.com",
        "phone": "256-245-2643",
    },
}

patient_2 = PatientData(**patient_data_2)

# Function calls
add_patient_data(patient_1)
add_patient_data(patient_2)

#--------------------------------------------------------------------------

#Required and optional field

from typing import List , Optional 
from pydantic import BaseModel

class PatientData(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_info: dict[str, str]


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully\n")


def update_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print("Data updated successfully\n")


# Patient 1
patient_data_1 = {
    "name": "John",
    "age": 25,
    "weight": 51.25,
    "married": True,
    "contact_info": {
        "email": "john5366@gmail.com",
        "phone": "354-168-2458",
    },
}

patient_1 = PatientData(**patient_data_1)


# Patient 2
patient_data_2 = {
    "name": "Alex",
    "age": 45,
    "weight": 67.25,
    "married": False,
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {
        "email": "alex366@gmail.com",
        "phone": "256-245-2643",
    },
}

patient_2 = PatientData(**patient_data_2)

# Function calls
add_patient_data(patient_1)
add_patient_data(patient_2)

#----------------------------------------------------------------------

#Data Validation

from pydantic import BaseModel , EmailStr , AnyUrl , Field
from typing import List , Optional 

class PatientData(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr
    linkedin_url : AnyUrl
    age: int = Field(gt=0 , lt=100)
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = Field(max_length=5)
    contact_info: dict[str, str]

def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully\n")

# Patient 1
patient_data_1 = {
    "name": "John",
    "email": "john1458@gmail.com",
    "linkedin_url":"https://www.linkedin.com",
    "age": 25,
    "weight": 51.25,
    "married": True,
    "contact_info": {
        "phone": "354-168-2458",
    },
}

patient_1 = PatientData(**patient_data_1)
add_patient_data(patient_1)

#------------------------------------------------------------------

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional, Annotated


class PatientData(BaseModel):
    name: Annotated[str,Field(max_length=50,title="Name of the patient",description="Give the name of the patient in less than 50 characters",examples=["John", "Alex"])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=100)
    weight: Annotated[float,Field(gt=0,strict=True,description="Weight of the patient in kg")]
    married: Annotated[bool,Field(default=None, description="Is the patient married or not")]
    allergies: Annotated[Optional[List[str]],Field(default=None, max_length=5)]
    contact_info: dict[str, str]


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print("Data added successfully\n")


patient_data_1 = {
    "name": "John",
    "email": "john1458@gmail.com",
    "linkedin_url": "https://www.linkedin.com",
    "age": 25,
    "weight": 51.25,
    "married": True,
    "contact_info": {
        "phone": "354-168-2458"
    }
}

patient_1 = PatientData(**patient_data_1)

add_patient_data(patient_1)
#------------------------------------------------------------------------

#Field validator 

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List,Dict, Optional, Annotated

class PatientData(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_info: Dict[str,str]
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('email')
    @classmethod
    def email_validator(cls , value):
        valid_domains =['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
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
        "linkedin_url":"https://www.linkedin.com",
        "age": 25,
        "weight": 51.25,
        "married": True,
        "allergies": ["peanuts","shellfish"],
        "contact_info": {
            "phone": "354-168-2458",
        },}
    
    patient_1 = PatientData(**patient_data)
    add_patient_data(patient_1)
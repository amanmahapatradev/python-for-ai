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

from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import List, Dict


class PatientData(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
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
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Married:", patient.married)
    print("Allergies:", patient.allergies)
    print("Contact Info:", patient.contact_info)
    print("LinkedIn:", patient.linkedin_url)


patient_data = {
    "name": "John",
    "email": "john1458@gmail.com",
    "linkedin_url": "https://www.linkedin.com",
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

#------------------------------------------------------------------------

#Model Validator

from pydantic import BaseModel, EmailStr, AnyUrl, field_validator , model_validator
from typing import List, Dict
class PatientData(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
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
    @model_validator(mode='after')
    def validate_emergency_contact(cls, mode):
        if mode.age > 60 and 'emergency' not in mode.contact_details:
            raise ValueError('Patient older then 60 must have aemergency contact ')
        return mode 

def add_patient_data(patient: PatientData):
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Married:", patient.married)
    print("Allergies:", patient.allergies)
    print("Contact Info:", patient.contact_info)
    print("LinkedIn:", patient.linkedin_url)


patient_data = {
    "name": "John",
    "email": "john1458@gmail.com",
    "linkedin_url": "https://www.linkedin.com",
    "age": 75,
    "weight": 51.25,
    "married": True,
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {
        "phone": "354-168-2458",
        "emergency": "322-458-3165"
    }
}

patient_1 = PatientData(**patient_data)
add_patient_data(patient_1)

# Another thing of model variable

from pydantic import BaseModel, EmailStr, AnyUrl, field_validator , model_validator
from typing import List, Dict
class PatientData(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_info: Dict[str, str]

    # @field_validator("name")
    # @classmethod
    # def transform_name(cls, value):
    #     return value.upper()

    # @field_validator("email")
    # @classmethod
    # def email_validator(cls, value):
    #     valid_domains = ["gmail.com", "hdfc.com", "icici.com"]
    #     domain_name = str(value).split("@")[-1].lower()
    #     if domain_name not in valid_domains:
    #         raise ValueError("Not a valid domain")
    #     return value
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, mode):
        if mode.age > 60 and 'emergency' not in mode.contact_details:
            raise ValueError('Patient older then 60 must have aemergency contact ')
        return mode 

def add_patient_data(patient: PatientData):
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Married:", patient.married)
    print("Allergies:", patient.allergies)
    print("Contact Info:", patient.contact_info)
    print("LinkedIn:", patient.linkedin_url)


patient_data = {
    "name": "John",
    "email": "john1458@gmail.com",
    "linkedin_url": "https://www.linkedin.com",
    "age": 75,
    "weight": 51.25,
    "married": True,
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {
        "phone": "354-168-2458",
        "emergency": "322-458-3165"
    }
}

patient_1 = PatientData(**patient_data)
add_patient_data(patient_1)

#--------------------------------------------------------------------------------------
# Computed Fields

from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class PatientData(BaseModel):
    
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_info: Dict[str , str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def add_patient_data(patient: PatientData):
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("Linkedin:", patient.linkedin_url)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Height:", patient.height)
    print("Married:", patient.married)
    print("Allergies:", patient.allergies)
    print("Contact Info:", patient.contact_info)
    print("BMI:", patient.bmi)
    print("Data added successfully to the database !")
    
patient_data = {"name": "John",
    "email": "john1458@gmail.com",
    "linkedin_url": "https://www.linkedin.com",
    "age": 75,
    "weight": 51.25,
    "height": 1.75,
    "married": True,
    "allergies": ["peanuts", "shellfish"],
    "contact_info": {
        "phone": "354-168-2458",
        "emergency": "322-458-3165"
    }
}

patient_1 = PatientData(**patient_data)
add_patient_data(patient_1)

#---------------------------------------------------------------------
# Nested Models

from pydantic import BaseModel
class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patientdata(BaseModel):
    
    name: str
    gender: str
    age: int 
    address: Address
    
address_dict = {'city':'gurgaon',
                'state': 'harayana',
                'pin': '122001'}

address1 = Address(**address_dict)
patient_dict = {'name': 'Himanshu',
                'gender': 'male',
                'age': 24,
                'address': address1}

patient1 = Patientdata(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address)
print(patient1.address.city)

#-----------------------------------------------------------------------
# Serilization


from pydantic import BaseModel
class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patientdata(BaseModel):
    
    name: str
    gender: str
    age: int 
    address: Address
    
address_dict = {'city':'gurgaon',
                'state': 'harayana',
                'pin': '122001'}

address1 = Address(**address_dict)
patient_dict = {'name': 'Himanshu',
                'gender': 'male',
                'age': 24,
                'address': address1}

patient1 = Patientdata(**patient_dict)

temp = patient1.model_dump()
# temp = patient1.model_dump_json()

print(temp)
print(type(temp))

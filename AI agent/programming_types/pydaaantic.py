from pydantic import BaseModel

class PatientData(BaseModel):
    name: str
    age: int
    
def add_patient_data():
    
    name: "Soumya"
    age: 25
    

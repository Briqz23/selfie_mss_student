import datetime
from typing import List
from src.domain.enums.state_enum import STATE
from src.domain.entities.selfie import Selfie
from src.domain.entities.student import Student

class StudentViewModel:
    ra: str
    name: str
    email: str
    
    def __init__(self, student: Student):
        self.ra = student.ra
        self.name = student.name
        self.email = student.email

    def to_dict(self) -> dict:
        return  {
            "ra":self.ra,
            "name":self.name,
            "email":self.email
        }

class CreateSelfieViewModel:
    idSelfie: int
    url: str
    dateUpload: datetime.datetime
    state: STATE
    student: StudentViewModel

    def __init__(self, data: Selfie):
        self.idSelfie = data.idSelfie
        self.url = data.url
        self.dateUpload = data.dateUpload
        self.state = data.state
        self.student = StudentViewModel(data.student)
        
    def to_dict(self) -> dict:
        return {
            "student": self.student.to_dict(),
            "idSelfie": self.idSelfie,
            "url": self.url,
            "dateUpload": self.dateUpload.isoformat(),
            "state": self.state.value,
            "message": "the selfie was created"
        }
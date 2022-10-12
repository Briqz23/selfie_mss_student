from src.domain.entities.student import Student


class UpdateStudentViewModel():

    def __init__(self, student: Student ):
        self.ra = student.ra
        self.name = student.name
        self.email = student.email


    def to_dict(self) -> dict:
        return {
            "ra": self.ra,
            "email": self.email,
            "name": self.name,
            "message": "User was updated successfully"
        }

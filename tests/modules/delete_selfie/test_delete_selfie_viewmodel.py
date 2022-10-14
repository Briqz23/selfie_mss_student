import pytest
from src.shared.domain.entities.student import Student
from src.shared.infra.repositories.student_repository_mock import StudentRepositoryMock
from src.modules.delete_selfie.delete_selfie_viewmodel import DeleteSelfieViewModel

class Test_DeleteSelfieViewModel:
    def test_get_selfie_view_model(self):
        repo = StudentRepositoryMock()
        selfie = repo.selfies[0]
        student = repo.students[0]
        result = {
            'student':{
            "ra":"21010757",
            "name":"Victor",
            "email":"eusousoller@gmail.com"
        },
            'selfie':{
            'dateUpload': '2022-10-12T16:01:59.149927',
            'idSelfie': 0,
            'state': 'DECLINED',
            'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            },
            'message':"the selfie was deleted"
          }
     


        
        studentViewModel = DeleteSelfieViewModel(data=selfie, student=student).to_dict()
        
        assert studentViewModel == result
        
        
from src.shared.domain.entities.student import Student
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.domain.enums.state_enum import STATE
from src.shared.domain.entities.selfie import Selfie
import datetime
import pytest

class Test_Selfie():
    def test_selfie(self):
        
        student = Student(
                ra="17090212",
                name="Monkey Guy",
                email="uuaa@floresta.com"
            )        
        
        dateUpload = datetime.datetime.now()
        
        selfie = Selfie (
                        student = student,
                        dateUpload= dateUpload,
                        url= "www.maua.br",
                        state= STATE.APPROVED,
                        idSelfie= 1
                        )
        
        assert type(selfie) == Selfie
        assert selfie.student == student
        assert selfie.dateUpload == dateUpload
        assert selfie.state == STATE.APPROVED

    def test_selfie_error(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17.090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                )  ,
                dateUpload= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= 1
            )

        
    def test_selfie_error_ra_int(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra=17090212,
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                )  ,
                dateUpload= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= 1
            )
      
    def test_selfie_error_url_invalid(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                )  ,
                dateUpload= datetime.datetime.now(),
                url= None,
                state= STATE.PENDING_REVIEW,
                idSelfie= 1
            )
        
    def test_selfie_error_state_invalid(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateUpload= datetime.datetime.now(),
                url= "www.maua.br",
                state= "PENDING_REVIEW",
                idSelfie= 1
            )
      
    def test_selfie_error_id_invalid(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateUpload= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= None
            )
        
    def test_selfie_error_id_invalid_str(self):
      with pytest.raises(EntityError):
        selfie = Selfie(
                student= Student(
                                ra="17090212",
                                name="Monkey Guy",
                                email="uuaa@floresta.com"
                                ),
                dateUpload= datetime.datetime.now(),
                url= "www.maua.br",
                state= STATE.PENDING_REVIEW,
                idSelfie= "1"
            )
      
import abc

from attr import validate
from src.helpers.errors.domain_errors import EntityError, EntityParameterTypeError


class Student(abc.ABC):
    ra: str
    name: str
    email: str

    def __init__(self, ra: str, name: str, email: str):
        if not Student.validate_ra(ra):
            raise EntityError('ra')
        self.ra = ra

        if len(name) == 0:
            raise EntityError('name')
        self.name = name

        if '@' not in email or '.' not in email:
            raise EntityError('email')
        self.email = email

    @staticmethod
    def validate_ra(ra: str) -> bool:
        if type(ra) != str:
            raise EntityParameterTypeError('ra must be a string')

        return ra.isdecimal() and len(ra) == 8 and ra != None

from dataclasses import replace
from src.domain.entities.student import Student
from src.helpers.errors.usecase_errors import NoItemsFound
from src.helpers.errors.controller_errors import MissingParameters
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.modules.get_student.get_student_usecase import GetStudentUsecase
from src.modules.get_student.get_student_view_model import GetStudentViewModel


class GetStudentController:
    def __init__(self, usecase: GetStudentUsecase):
        self.getStudentUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')

            student = self.getStudentUsecase(
                ra=request.query_params["ra"]
            )
            viewmodel = GetStudentViewModel(student)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0].message)

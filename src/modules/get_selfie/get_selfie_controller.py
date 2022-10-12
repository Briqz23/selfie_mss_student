from src.domain.entities.student import Student
from src.domain.entities.selfie import Selfie
from src.helpers.errors.domain_errors import EntityError
from src.helpers.errors.usecase_errors import NoItemsFound
from src.helpers.errors.controller_errors import MissingParameters
from src.helpers.http.http_models import OK, BadRequest, HttpRequest, HttpResponse, InternalServerError, NotFound
from src.modules.get_selfie.get_selfie_viewmodel import GetSelfieViewModel
from src.modules.get_selfie.get_selfie_usecase import GetSelfieUsecase


class GetSelfieController:
    def __init__(self, usecase: GetSelfieUsecase):
        self.getSelfieUsecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')

            if request.query_params.get('idSelfie') is None:
                raise MissingParameters('idSelfie')

            selfie = self.getSelfieUsecase(
                ra=request.query_params.get('ra'),
                idSelfie=request.query_params.get('idSelfie')
                )
            viewmodel = GetSelfieViewModel(selfie)
            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])

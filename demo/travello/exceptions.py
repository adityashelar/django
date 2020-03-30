from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

class DataNotFoundException(APIException):
    status_code = 400
    default_detail = "No data found"
    default_code = "bad_request"


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['newItem'] = response.status_code
    return response
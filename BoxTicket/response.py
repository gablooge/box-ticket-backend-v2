from rest_framework.response import Response


def customResponse(
    response, end_error_message="", error_message="", error_code=0, method_status=True
):
    response.update(
        {
            "EndErrorMessge": end_error_message,
            "ErrorCode": error_code,
            "ErrorMessage": error_message,
            "MethodStatus": method_status,
        }
    )
    return Response(response)

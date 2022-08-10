from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        message = ""
        success = False
        response_status = ""

        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            message = "Logout successfully."
            response_status = status.HTTP_200_OK
            success = True
        except Exception:
            message = "Refresh Token not valid"
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(
            data={"success": success, "message": message},
            status=response_status,
        )

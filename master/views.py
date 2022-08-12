from rest_framework.views import APIView
from BoxTicket.response import customResponse
from master.models import Country
from master.serializers import CountrySerializers


class CountryView(APIView):
    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializers(countries, many=True)
        if countries.count() == 0:
            end_error_message = "No Data Found"
            error_message = "No Data Found"
            error_code = 1
            method_status = False
            return customResponse(
                {"CountriesList": serializer.data},
                end_error_message,
                error_message,
                error_code,
                method_status,
            )
        return customResponse({"CountriesList": serializer.data})

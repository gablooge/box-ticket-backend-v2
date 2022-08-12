from rest_framework.viewsets import ReadOnlyModelViewSet
from BoxTicket.response import customResponse
from master.models import Country
from master.serializers import CountrySerializers


class CountryView(ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers

    def list(self, request):
        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.get_queryset(), many=True)
        if not serializer.data:
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
        return customResponse({"RegionsList": serializer.data})

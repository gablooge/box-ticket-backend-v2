from rest_framework.viewsets import ReadOnlyModelViewSet
from BoxTicket.response import customResponse
from master.models import Country, Region, City
from master.serializers import CountrySerializers, RegionSerializers, CitySerializers


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


class RegionView(ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializers

    def get_queryset(self):
        country_id = self.request.GET.get("country_id", None)
        queryset = self.queryset
        if country_id:
            try:
                country_id = int(country_id)
                queryset = queryset.filter(country__id=country_id)
            except Exception:
                queryset = {}
        return queryset

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
                {"RegionsList": serializer.data},
                end_error_message,
                error_message,
                error_code,
                method_status,
            )
        return customResponse({"RegionsList": serializer.data})


class CityView(ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializers

    def get_queryset(self):
        region_id = self.request.GET.get("region_id", None)
        queryset = self.queryset
        if region_id:
            try:
                region_id = int(region_id)
                queryset = queryset.filter(region__id=region_id)
            except Exception:
                queryset = {}
        return queryset

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
                {"CitiesList": serializer.data},
                end_error_message,
                error_message,
                error_code,
                method_status,
            )
        return customResponse({"CitiesList": serializer.data})

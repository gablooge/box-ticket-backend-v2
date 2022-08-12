from django.urls import path
from master.views import CountryView, RegionView

urlpatterns = [
    path("GetCountries/", CountryView.as_view(), name="get_countries"),
    path("GetRegions/", RegionView.as_view(), name="get_regions"),
]

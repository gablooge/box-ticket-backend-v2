from django.urls import path
from master.views import CountryView

urlpatterns = [path("GetCountries/", CountryView.as_view(), name="get_countries")]

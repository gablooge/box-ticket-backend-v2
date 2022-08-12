from master.views import CountryView
from rest_framework import routers

router = routers.DefaultRouter()

router.register("GetCountries", CountryView)

urlpatterns = router.urls

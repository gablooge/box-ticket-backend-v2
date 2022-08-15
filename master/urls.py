from master.views import CountryView, RegionView, CityView
from rest_framework import routers

router = routers.DefaultRouter()

router.register("GetCountries", CountryView)
router.register("GetRegions", RegionView)
router.register("GetCities", CityView)

urlpatterns = router.urls

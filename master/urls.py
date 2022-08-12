from master.views import CountryView, RegionView, CityView, MenuView
from rest_framework import routers

router = routers.DefaultRouter()

router.register("GetCountries", CountryView)
router.register("GetRegions", RegionView)
router.register("GetCities", CityView)
router.register("GetMenu", MenuView)

urlpatterns = router.urls

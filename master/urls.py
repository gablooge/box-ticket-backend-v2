from master.views import CountryView, RegionView
from rest_framework import routers

router = routers.DefaultRouter()

router.register("GetCountries", CountryView)
router.register("GetRegions", RegionView)

urlpatterns = router.urls

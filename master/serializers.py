from rest_framework import serializers
from master.models import Country, Region


class CountrySerializers(serializers.ModelSerializer):
    country_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Country
        fields = ("country_id", "country_name")
        read_only_fields = ["country_id"]

    def get_country_id(self, obj):
        return obj.pk


class RegionSerializers(serializers.ModelSerializer):
    region_id = serializers.SerializerMethodField(read_only=True)
    country_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Region
        fields = ("region_id", "country_id", "region_name")
        read_only_fields = ["region_id", "country_id"]

    def get_region_id(self, obj):
        return obj.pk

    def get_country_id(self, obj):
        return obj.country.pk

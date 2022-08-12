from rest_framework import serializers
from master.models import City, Country, Menu, Region


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


class CitySerializers(serializers.ModelSerializer):
    region_id = serializers.SerializerMethodField(read_only=True)
    country_id = serializers.SerializerMethodField(read_only=True)
    city_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = City
        fields = ("region_id", "country_id", "city_id", "city_name")
        read_only_fields = ["region_id", "country_id", "city_id"]

    def get_region_id(self, obj):
        return obj.region.pk

    def get_country_id(self, obj):
        return obj.region.country.pk

    def get_city_id(self, obj):
        return obj.pk


class MenuSerializers(serializers.ModelSerializer):
    ID = serializers.SerializerMethodField(read_only=True)
    Description = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Menu
        fields = ("ID", "Description")
        read_only_fields = ["ID"]

    def get_ID(self, obj):
        return obj.pk

    def get_Description(self, obj):
        return obj.description

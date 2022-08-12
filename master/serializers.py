from rest_framework import serializers
from master.models import Country


class CountrySerializers(serializers.ModelSerializer):
    country_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Country
        fields = ("country_id", "country_name")
        read_only_fields = ["country_id"]

    def get_country_id(self, obj):
        return obj.pk

from rest_framework import serializers

from weather.models import Weather, StatsModel


class WeatherSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = [
            "station_id",
            "date",
            "max_temp",
            "min_temp",
            "precipitation",
            "created_timestamp",
            "updated_timestamp",
        ]


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsModel
        fields = [
            "station_id",
            "year",
            "avg_max_temp",
            "avg_min_temp",
            "total_precipitation",
            "created_timestamp",
            "updated_timestamp",
        ]

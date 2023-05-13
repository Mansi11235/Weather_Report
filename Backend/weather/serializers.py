from rest_framework import serializers
from weather.models import Weather, Statistics


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['date','maximum_temp', 'minimum_temp', 'precipitation','state_code']

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['year', 'average_minimum', 'average_maximum', 'total_precipitation', 'state_code']
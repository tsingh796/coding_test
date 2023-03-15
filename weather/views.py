from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from weather.commons.weather_stats import WeatherStats
from weather.models import Weather, StatsModel
from weather.serializers import WeatherSeriliazer, StatsSerializer


class ListWeatherView(ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSeriliazer


class AnalyzeWeather(APIView):
    def get(self, req):
        weather_stats = WeatherStats()
        weather_stats.handle()
        return Response({"Message": "Weather analysis Successfull"})



class StatsView(ListAPIView):
    queryset = StatsModel.objects.all()
    serializer_class = StatsSerializer
from django.urls import path

from weather.views import ListWeatherView, AnalyzeWeather, StatsView


urlpatterns = [
    path("weather", ListWeatherView.as_view(), name="list_weather"),
    path("analyze", AnalyzeWeather.as_view(), name="analyze_weather"),
    path("weather/stats", StatsView.as_view(), name="stats_list"),
]

from django.urls import path
from weather import views
# from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('api/weather/', views.WeatherDetail.as_view()),
    path('api/weather/stats/', views.StatisticsDetail.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)
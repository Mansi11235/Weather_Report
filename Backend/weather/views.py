from rest_framework.response import Response
from django.http import Http404, HttpRequest
from weather.models import Weather, Statistics
from rest_framework.views import APIView
from weather.serializers import WeatherSerializer, StatisticsSerializer


class WeatherDetail(APIView):
    
    def get_object(self, date, place):
        try:
            weather = Weather.objects.filter(date=date).filter(state_code=place)
            return weather
        except Weather.DoesNotExist:
            raise Http404
        
    def get_object_by_date(self, date):
        try:
            data = Weather.objects.filter(date=date)
            return data
        except Weather.DoesNotExist:
            raise Http404
        
    def get_object_by_state(self, place):
        try:
            data = Weather.objects.filter(state_code=place)
            return data
        except Weather.DoesNotExist:
            raise Http404
        
    def get_all_objects(self):
        try:
            data = Weather.objects.all()
            return data
        except Weather.DoesNotExist:
            raise Http404
        
    def get(self, request, format=None):
        # weatherobj = request.query_params
        if "date" in request.GET and "state_code" not in request.GET:
            date = request.GET['date']
            data = self.get_object_by_date(date=date)
        elif "state_code" in request.GET and "date" not in request.GET:
            place = request.GET['state_code'].upper()
            data = self.get_object_by_state(place=place)
        elif "date" in request.GET and "state_code" in request.GET:
            date = request.GET['date'] 
            place = request.GET['state_code'].upper()
            data = self.get_object(date=date, place=place)
        else:
            data = self.get_all_objects()
 
        serializer = WeatherSerializer(data, many=True)
        return Response(serializer.data)

    def __str__(self):
        return self.date

class StatisticsDetail(APIView):
    def get_object(self, year, place):
        try:
            data = Statistics.objects.filter(year=year).filter(state_code=place)
            return data
        except Weather.DoesNotExist:
            raise Http404
        
    def get_object_by_year(self, year):
        try:
            data = Statistics.objects.filter(year=year)
            return data
        except Weather.DoesNotExist:
            raise Http404
        
    def get_object_by_state(self, place):
        try:
            data = Statistics.objects.filter(state_code=place)
            return data
        except Weather.DoesNotExist:
            raise Http404
        
    def get_all_objects(self):
        try:
            data = Statistics.objects.all()
            return data
        except Statistics.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        
        if "year" in request.GET and "state_code" not in request.GET:
            year = request.GET['year']
            data = self.get_object_by_year(year=year)
            
        elif "state_code" in request.GET and "year" not in request.GET:
            place = request.GET['state_code'].upper()
            data = self.get_object_by_state(place=place)
            
        elif "year" in request.GET and "state_code" in request.GET:
            year = request.GET['year'] 
            place = request.GET['state_code'].upper()
            data = self.get_object(year=year, place=place)
            
        else:
            data = self.get_all_objects()

        serializer = StatisticsSerializer(data, many=True)
        return Response(serializer.data)
    

    def __str__(self):
        return self.year
    


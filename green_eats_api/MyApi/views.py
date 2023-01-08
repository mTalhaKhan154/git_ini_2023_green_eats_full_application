from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from MyApi.serializers import ImageRequestSerializer
from MyApi.models import getData


class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = getData.objects.all().order_by('date_created')
    serializer_class = ImageRequestSerializer
# Create your views here.
def api(request):
  data = {
    "name":"Mohammad talha khan", 
    "Class":11
  }
  return JsonResponse(data)
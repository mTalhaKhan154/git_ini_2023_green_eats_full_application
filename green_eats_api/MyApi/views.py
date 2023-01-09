from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from MyApi.serializers import ImageRequestSerializer
from MyApi.models import getData
from django.conf import settings



class DataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = getData.objects.all().order_by('date_created')
    serializer_class = ImageRequestSerializer
# Create your views here.
def modelPredict():
  from keras.models import load_model
  model = load_model(settings.MODEL_FILE_PATH)
  image = "./media/foodimages/1072416.jpg" # get the image from the request
  prediction = "hello"
  prediction = model.predict(image)
  print(prediction)
  print("did not work")
def api(request):
  return HttpResponse(modelPredict())
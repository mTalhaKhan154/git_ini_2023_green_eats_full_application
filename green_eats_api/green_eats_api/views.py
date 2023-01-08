from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponseNotFound
def home_page(request):
  return HttpResponseNotFound("Page not found")
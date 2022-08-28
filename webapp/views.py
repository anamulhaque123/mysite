from django.shortcuts import render
from .models import address

# Create your views here.
def index(request):
  name = address.objects.all
  return  render(request, 'index.html',{'name':name})
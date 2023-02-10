from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Detail
from .serializer import DetailSerializer
import requests

#creating my first REST API here
@api_view(['GET'])
def GetDetail(request):
    name = Detail.objects.all()
    serializer = DetailSerializer(name, many=True)
    return Response(serializer.data)

# Create your views here.
def index(request):
    varables = {
        "temp_no" : 1
    }
    return render(request, 'index.html', varables)
    # return HttpResponse('This is the start')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is the About')

def know(request):
    response = requests.get('http://127.0.0.1:8000/post/')
    data = response.json()
    return render(request, 'know.html', {'data': data})

def contact(request):
    return render(request, 'contact.html')
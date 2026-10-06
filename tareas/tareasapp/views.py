from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    response_test = "HOLAAAAA"

    return HttpResponse(response_test)
    pass
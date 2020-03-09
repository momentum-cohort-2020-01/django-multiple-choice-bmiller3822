from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Snippet, Category, Library

def index(request):
	return HttpResponse ('This is just a text response, unrelated to the database.') 


# Create your views here.

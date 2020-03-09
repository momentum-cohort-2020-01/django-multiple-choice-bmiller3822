from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Snippet, Category, Library

@login_required
def snippets(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/snippets.html', {'snippets': snippets})

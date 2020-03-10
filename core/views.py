from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Snippet, Category, Library

from .forms import SnippetForm

@login_required
def snippets(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/snippets.html', {'snippets': snippets})


def add_snippet(request):
    snippets = Snippet.objects.all()
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            return redirect('snippets')
    else:
        form = SnippetForm()
    
    return render(request, 'core/new_snippet.html', {'form': form, 'snippets': snippets})


def edit_snippet(request, pk):
    snippets = Snippet.objects.all()
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save()
            return redirect('snippets')
    else:
        form = SnippetForm(instance=snippet)

    return render(request, 'core/edit_snippet.html', {'form': form, 'snippets': snippets})

def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return redirect('/')
    
def snippets_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    snippets_for_category = snippets.objects.filter(category=category)
    return render(request, 'core/snippets_by_category', {'category': category})


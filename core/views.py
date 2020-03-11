from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from .models import Snippet, Category, Library

from .forms import SnippetForm

@login_required
def snippets(request):
    snippets = Snippet.objects.all()

    def sql_query(query_string):
        """
        Splits string from front-end into individual words and creates SQL query that looks for those keywords in title, description, category, or code.
        """
        query_terms = query_string.split(" ")
        sql_query = Q()
        for term in query_terms:
            sql_query = sql_query | Q(
                category__category_name__icontains=term) | Q(snippet_title__icontains=term) | Q(description__icontains=term) | Q(code__icontains=term)
        return sql_query
    context = {}
    query = request.GET.get('q')
    if query:
        snippets = Snippet.objects.filter(sql_query(query))
    else:
        snippets = Snippet.objects.all
    context['query'] = str(query)
    return render(request, 'core/snippets.html', {'snippets': snippets})


def snippet_detail(request, pk):
    snippets = Snippet.objects.all()
    snippet = Snippet.objects.get(pk=pk)
    return render(request, 'core/snippet_detail.html', {'snippet': snippet, 'pk': pk})


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
    snippets_for_category = Snippet.objects.filter(category=category)
    return render(request, 'core/snippets_by_category.html', {'snippets': snippets_for_category, 'category': category})

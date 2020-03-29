from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Article
from .forms import ArticleForm


class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'detail_page'


def edit_page(request):
    success = False
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    template = 'edit_page.html'
    context = {
        'list_articles': Article.objects.all().order_by('-id'),
        'form': ArticleForm(),
        'success': success
    }
    return render(request, template, context)


def update_page(request, pk):
    get_article = Article.objects.get(pk=pk)
    success_update = False

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            success_update = True


    template = 'edit_page.html'
    context = {
        'get_article': get_article,
        'update': True,
        'form': ArticleForm(instance=get_article),
        'success_update': success_update
    }
    return render(request, template, context)

def delete_page(request, pk):
    get_article = Article.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('edit_page'))


from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from django_study_project.women.forms import AddPostForm
from django_study_project.women.models import Women, Category



menu = [{'title': 'About', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'}]


class WomenIndex(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        context['cat_selected'] = 0       
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        return Women.objects.filter(is_published=True)


# How it was in function
# def index(request):
#     posts = Women.objects.all()
#     return render(request, 'women/index.html', context={
#         'title': 'Main page',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': 0,
#     })


def about(request):
    return render(request, 'women/about.html', context={
        'title': 'About',
        'menu': menu
    })


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    succes_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add page'      
        return context


# How it was in function
# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()

#     return render(request, 'women/addpage.html', context={
#         'form': form,
#         'menu': menu,
#         'title': 'Add page'
#     })


def contact(request):
    return HttpResponse('contact')


def login(request):
    return HttpResponse('login')


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']   
        return context


# How it was in function
# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     return render(request, 'women/post.html', context={
#         'post': post,
#         'menu': menu,
#         'title': post.name,
#         'cat_selected': post.cat_id,
#     })



class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Category - ' + str(context['posts'][0].cat) 
        context['cat_selected'] = context['posts'][0].cat_id      
        return context


# How it was in function
# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     return render(request, 'women/index.html', context={
#         'title': 'Articles',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': cat_id,
#     })


def pageNotFound(request, exeption):
    return HttpResponseNotFound('Page not found')

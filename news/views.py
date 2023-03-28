from django.shortcuts import render
from django.views.generic import ListView
from .models import News
# Create your views here.
class HomePageView(ListView):
    model=News
    template_name='home.html'
    context_object_name='all_post_list'


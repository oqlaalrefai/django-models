from django.shortcuts import render
from django.views.generic import(ListView, DetailView)
from .models import snack

# Create your views here.

class snackList(ListView):
    template_name = 'snack_list.html'
    model = snack
    context_object_name = 'snacks'

class snackDetail(DetailView):
    template_name = 'snack_detail.html'
    model = snack
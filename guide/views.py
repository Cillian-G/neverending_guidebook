from django.shortcuts import render
from django.views import generic
from .models import Location   


class PreviewList(generic.ListView):
    model = Location
    queryset = Location.objects.order_by('title')
    template_name = 'index.html'

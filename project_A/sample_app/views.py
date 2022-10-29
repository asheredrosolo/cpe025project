from django.shortcuts import render
from .models import sample_db
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

# Create your views here.

def home(request):
    context = {
        'key': sample_db.objects.all()
    }
    return render(request, "sample_app/home.html", context)

class DataListView(ListView):
    model = sample_db
    template_name = 'sample_app/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'key'
    ordering = ['-date']

class DataDetailView(DetailView):
    model = sample_db

class DataCreateView(CreateView):
    model = sample_db
    fields = ['title', 'content']

def about(request):
    return render(request, "sample_app/about.html", {'title': 'About'} )

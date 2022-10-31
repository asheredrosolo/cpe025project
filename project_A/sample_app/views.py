from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import sample_db
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# Create your views here.
@login_required
def home(request):
    context = {
        'key': sample_db.objects.all()
    }
    return render(request, "sample_app/home.html", context)

class DataListView(LoginRequiredMixin, ListView):
    model = sample_db
    template_name = 'sample_app/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'key'
    ordering = ['-date']
    paginate_by = 5

class UserDataListView(LoginRequiredMixin, ListView):
    model = sample_db
    template_name = 'sample_app/user_data.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'key'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return sample_db.objects.filter(author=user).order_by('-date')

class DataDetailView(LoginRequiredMixin, DetailView):
    model = sample_db

class DataCreateView(LoginRequiredMixin, CreateView):
    model = sample_db
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DataUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = sample_db
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        data = self.get_object()
        if self.request.user == data.author:
            return True
        return False

class DataDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = sample_db
    success_url = '/'

    def test_func(self):
        data = self.get_object()
        if self.request.user == data.author:
            return True
        return False


def about(request):
    return render(request, "sample_app/about.html", {'title': 'About'} )

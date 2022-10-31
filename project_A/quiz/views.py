from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import questions, modules
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

# Create your views here.

#===================================================================================
#           MODULES VIEW
#===================================================================================

@login_required
def module_view(request):
    module_items = {
        'key': modules.objects.all()
    }
    return render(request, "quiz/module.html", module_items)

class ModuleListView(LoginRequiredMixin, ListView):
    model = modules
    template_name = 'quiz/module.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'key'
    ordering = ['module']

class ModuleCreateView(LoginRequiredMixin, CreateView):
    model = modules
    fields = ['module']

    def form_valid(self, form):
        return super().form_valid(form)

class ModuleDetailView(LoginRequiredMixin, DetailView):
    model = modules

class ModuleUpdateView(LoginRequiredMixin, UpdateView):
    model = modules
    fields = ['module']

    def form_valid(self, form):
        return super().form_valid(form)

class ModuleDeleteView(LoginRequiredMixin, DeleteView):
    model = modules
    success_url = '/quiz/modules/'

#===================================================================================
#           QUESTIONS VIEW
#===================================================================================

@login_required
def question_view(request):
    context = {
        'key': questions.objects.all()
    }
    return render(request, "quiz/questions.html", context)

class QuestionListView(LoginRequiredMixin, ListView):
    model = questions
    template_name = 'quiz/questions.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'key'
    ordering = ['question']

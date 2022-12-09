from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import modules, category, trueorfalse, mcq, identification, quiz
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
    cat1 = mcq.objects.all()
    cat2 = trueorfalse.objects.all()
    cat3 = identification.objects.all()
    return render(request, "quiz/questions.html", {'cat1': cat1, 'cat2': cat2, 'cat3': cat3})

def cat_selection(request):
    return render(request, 'quiz/question_selection.html')

#-----------------------------------------------------------------------------------
#           DETAIL VIEW
#-----------------------------------------------------------------------------------

class MCQDetailView(LoginRequiredMixin, DetailView):
    model = mcq
    template_name = 'quiz/mcq_detail.html'

class TOFDetailView(LoginRequiredMixin, DetailView):
    model = trueorfalse
    template_name = 'quiz/tof_detail.html'

class IdentificationDetailView(LoginRequiredMixin, DetailView):
    model = identification
    template_name = 'quiz/identification_detail.html'

#-----------------------------------------------------------------------------------
#           CREATE VIEW
#-----------------------------------------------------------------------------------

class MCQCreateView(LoginRequiredMixin, CreateView):
    model = mcq
    fields = ['question', 'module', 'option1', 'option2', 'option3', 'option4', 'answer']
    template_name = 'quiz/create_mcq.html'

    def form_valid(self, form):
        return super().form_valid(form)

class TOFCreateView(LoginRequiredMixin, CreateView):
    model = trueorfalse
    fields = ['question', 'module', 'answer']
    template_name = 'quiz/create_tof.html'

    def form_valid(self, form):
        return super().form_valid(form)

class IdentificationCreateView(LoginRequiredMixin, CreateView):
    model = identification
    fields = ['question', 'module', 'answer']
    template_name = 'quiz/create_identification.html'

    def form_valid(self, form):
        return super().form_valid(form)

#-----------------------------------------------------------------------------------
#           UPDATE VIEW
#-----------------------------------------------------------------------------------

class MCQUpdateView(LoginRequiredMixin, UpdateView):
    model = mcq
    fields = ['question', 'module', 'option1', 'option2', 'option3', 'option4', 'answer']
    template_name = 'quiz/create_mcq.html'

    def form_valid(self, form):
        return super().form_valid(form)

class TOFUpdateView(LoginRequiredMixin, UpdateView):
    model = trueorfalse
    fields = ['question', 'module', 'answer']
    template_name = 'quiz/create_tof.html'

    def form_valid(self, form):
        return super().form_valid(form)

class IdentificationUpdateView(LoginRequiredMixin, UpdateView):
    model = identification
    fields = ['question', 'module', 'answer']
    template_name = 'quiz/create_identification.html'

    def form_valid(self, form):
        return super().form_valid(form)

class MCQDeleteView(LoginRequiredMixin, DeleteView):
    model = mcq
    template_name = 'quiz/delete_mcq.html'
    success_url = '/quiz/questions/'

class TOFDeleteView(LoginRequiredMixin, DeleteView):
    model = trueorfalse
    template_name = 'quiz/delete_tof.html'
    success_url = '/quiz/questions/'

class IdentificationDeleteView(LoginRequiredMixin, DeleteView):
    model = identification
    template_name = 'quiz/delete_identification.html'
    success_url = '/quiz/questions/'
        
#===================================================================================
#           QUIZ VIEW
#===================================================================================

@login_required
def quiz_view(request):
    quiz_items = {
        'key': quiz.objects.all(),
    }
    return render(request, "quiz/quiz.html", quiz_items)

class QuizCreateView(LoginRequiredMixin, CreateView):
    model = quiz
    fields = ['quiz_title', 'module', 'mcq_questions', 'tof_questions', 'identification_questions' ]
    template_name = 'quiz/create_quiz.html'

    def form_valid(self, form):
        return super().form_valid(form)

class QuizDetailView(LoginRequiredMixin, DetailView):
    model = quiz
    template_name = 'quiz/quiz_detail.html'


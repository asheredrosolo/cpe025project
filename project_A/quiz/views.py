from io import BytesIO
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import (View, CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .models import (identification, mcq, modules, quizzes, scores,
                     trueorfalse)

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

#-----------------------------------------------------------------------------------
#           DELETE VIEW
#-----------------------------------------------------------------------------------

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
        'key': quizzes.objects.all(),
    }
    return render(request, "quiz/quiz.html", quiz_items)

class QuizCreateView(LoginRequiredMixin, CreateView):
    model = quizzes
    fields = ['quiz_title', 'module', 'mcq_questions', 'tof_questions', 'identification_questions' ]
    template_name = 'quiz/create_quiz.html'

class QuizTakeView(LoginRequiredMixin, DetailView):
    model = quizzes
    template_name = 'quiz/quiz_take.html'

class QuizListView(LoginRequiredMixin, ListView):
    model = quizzes
    template_name = 'quiz/quiz.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'key'
    ordering = ['quiz_title']

class QuizDetailView(LoginRequiredMixin, DetailView):
    model = quizzes
    template_name = 'quiz/quiz_edit.html'

class QuizUpdateView(LoginRequiredMixin, UpdateView):
    model = quizzes
    fields = ['quiz_title', 'module', 'mcq_questions', 'tof_questions', 'identification_questions' ]
    template_name = 'quiz/create_quiz.html'

    def form_valid(self, form):
        return super().form_valid(form)

class QuizDeleteView(LoginRequiredMixin, DeleteView):
    model = quizzes
    template_name = 'quiz/delete_quiz.html'
    success_url = '/quiz/quiz'

#===================================================================================
#           QUIZ ANSWERING AND SCORING
#===================================================================================

@login_required
def take_quiz(request, *args, **kwargs):

    if request.method == 'POST':
        print(request.POST)
        quiz = quizzes.objects.filter(id=kwargs['pk']).first()
        score=0
        wrong=0
        correct=0
        total=0

        for m in quiz.mcq_questions.all():
            total+=1
            answer = request.POST.get(m.question) # Gets user’s choice, i.e the key of answer
            items = vars(m) # Holds the value for choice
            if not request.POST.get(m.question):
                wrong+=1
            else:
                print(items[answer])
                if m.answer == items[answer]: # Compares actual answer with user’s choice
                    score+=1
                    correct+=1
                else:
                    wrong+=1
        
        for t in quiz.tof_questions.all():
            total+=1
            answer = request.POST.get(t.question) # Gets user’s choice, i.e the key of answer
            items = vars(t) # Holds the value for choice
            if not request.POST.get(t.question):
                wrong+=1
            else:
                #print(items[answer])
                if str(t.answer) == answer: # Compares actual answer with user’s choice
                    score+=1
                    correct+=1
                else:
                    wrong+=1
        for i in quiz.identification_questions.all():
            total+=1
            answer = request.POST.get(i.question) # Gets user’s choice, i.e the key of answer
            items = vars(i) # Holds the value for choice
            if not request.POST.get(i.question):
                wrong+=1
            else:
                #print(items[answer])
                if str(i.answer).lower() == str(answer).lower() : # Compares actual answer with user’s choice
                    score+=1
                    correct+=1
                else:
                    wrong+=1

        if total == 0:
            percent = 0/100
        else:
            percent = score/(total)*100
    
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent': percent,
            'total':total
        }

        scores.objects.create(
            user = request.user,
            quiz_title=quiz.quiz_title,
            score=score,
            correct=correct,
            wrong=wrong,
            total_items=total,
            )

        return render(request,'quiz/testresult.html',context)
    else:
        quiz = quizzes.objects.filter(id=kwargs['pk']).first()
        context = {
            'Quiz': quiz,
            'M': quiz.mcq_questions.all(),
            'T': quiz.tof_questions.all(),
            'I': quiz.identification_questions.all(),
        }
        return render(request,'quiz/take_quiz.html',context)

#===================================================================================
#           RENDER TO PDF
#===================================================================================

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class viewpdf(View):
    
    def get(self, request, *args, **kwargs):

        data = {
            'key': quizzes.objects.filter(id=kwargs['pk'])
        }

        pdf = render_to_pdf('quiz/pdfview.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class downloadpdf(View):
    def get(self, request, *args, **kwargs):

        data = {
            'key': quizzes.objects.filter(id=kwargs['pk'])
        }

        pdf = render_to_pdf('quiz/pdfview.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Test_%s.pdf" %("12345")
        content = "attachment: filename='%s'" %(filename)
        response['content-description'] = content
        return response

#===================================================================================
#           SCORING
#===================================================================================

@login_required
def quiz_view(request):
    context = {
        'key': scores.objects.all(),
    }
    return render(request, "quiz/scores.html", context)

class ScoreListView(LoginRequiredMixin, ListView):
    model = scores
    template_name = 'quiz/scores.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'key'
    ordering = ['date']




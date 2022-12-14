from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class modules(models.Model):
    module = models.CharField(max_length=50)

    def __str__(self):
        return self.module

    def get_absolute_url(self):
        return reverse('module')

class category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class TF(models.Model):
    choices = models.CharField(max_length=20)

    def __str__(self):
        return self.choices

class trueorfalse(models.Model):
    question = models.TextField()
    module = models.ForeignKey(modules, on_delete=models.CASCADE)
    answer = models.ForeignKey(TF, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question
    
    def get_absolute_url(self):
        return reverse('questions')

class mcq(models.Model):
    question = models.TextField()
    module = models.ForeignKey(modules, on_delete=models.CASCADE)
    option1 = models.CharField(blank=True ,max_length=255)
    option2 = models.CharField(blank=True, max_length=255)
    option3 = models.CharField(blank=True, max_length=255)
    option4 = models.CharField(blank=True, max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question
    
    def get_absolute_url(self):
        return reverse('questions')

class identification(models.Model):
    question = models.TextField()
    module = models.ForeignKey(modules, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question
    
    def get_absolute_url(self):
        return reverse('questions')

class quizzes(models.Model):
    quiz_title = models.CharField(max_length=2555)
    module = models.ForeignKey(modules, on_delete=models.CASCADE)
    mcq_questions = models.ManyToManyField(mcq, blank=True)
    tof_questions = models.ManyToManyField(trueorfalse, blank=True)
    identification_questions = models.ManyToManyField(identification, blank=True)

    def __str__(self):
        return self.quiz_title
    
    def get_absolute_url(self):
        return reverse('quiz')

class scores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_title = models.CharField(max_length=255)
    score = models.IntegerField()
    correct = models.IntegerField()
    wrong = models.IntegerField()
    total_items = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.quiz_title
    
    def get_absolute_url(self):
        return reverse('score-list')


    
    


from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
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

class questions(models.Model):
    question = models.TextField()
    module = models.ForeignKey(modules, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    option1 = models.CharField(blank=True ,max_length=255)
    option2 = models.CharField(blank=True, max_length=255)
    option3 = models.CharField(blank=True, max_length=255)
    option4 = models.CharField(blank=True, max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question
    
    


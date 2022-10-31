from django.contrib import admin
from .models import questions, modules, category

# Register your models here.
admin.site.register(questions)
admin.site.register(modules)
admin.site.register(category)
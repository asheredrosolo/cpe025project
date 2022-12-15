from xmlrpc.client import boolean
from django.contrib import admin
from .models import identification, mcq, modules, category, trueorfalse, TF, quizzes, scores

# Register your models here.
admin.site.register(modules)
admin.site.register(category)
admin.site.register(trueorfalse)
admin.site.register(TF)
admin.site.register(mcq)
admin.site.register(identification)
admin.site.register(quizzes)
admin.site.register(scores)
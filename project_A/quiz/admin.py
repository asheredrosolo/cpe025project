from xmlrpc.client import boolean
from django.contrib import admin
from .models import identification, mcq, modules, category, trueorfalse, TF, quiz

# Register your models here.
admin.site.register(modules)
admin.site.register(category)
admin.site.register(trueorfalse)
admin.site.register(TF)
admin.site.register(mcq)
admin.site.register(identification)
admin.site.register(quiz)
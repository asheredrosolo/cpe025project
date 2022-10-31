from django.urls import path
from . import views
from .views import (
    ModuleListView,
    ModuleCreateView,
    ModuleDetailView,
    ModuleUpdateView,
    ModuleDeleteView,
)

urlpatterns = [

#===================================================================================
#           MODULES URL
#===================================================================================

    path('modules/', ModuleListView.as_view(), name='module'),
    path('modules/create/', ModuleCreateView.as_view(), name='module-create'),
    path('modules/<int:pk>/', ModuleDetailView.as_view(), name = 'module-detail'),
    path('modules/<int:pk>/update/', ModuleUpdateView.as_view(), name = 'module-update'),
    path('modules/<int:pk>/delete/', ModuleDeleteView.as_view(), name = 'module-delete'),

#===================================================================================
#           QUESTIONS URL
#===================================================================================

    path('questions/', views.question_view, name='questions'),




    
]
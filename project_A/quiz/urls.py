from django.urls import path
from . import views
from .views import (
    ModuleListView, ModuleCreateView, ModuleDetailView, ModuleUpdateView, ModuleDeleteView, 
    MCQDetailView, MCQCreateView, MCQUpdateView, MCQDeleteView,
    TOFDetailView, TOFCreateView, TOFUpdateView, TOFDeleteView,
    IdentificationDetailView, IdentificationCreateView, IdentificationUpdateView, IdentificationDeleteView,
)

urlpatterns = [

    path('category/', views.cat_selection, name='category'),

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
    path('mcq/<int:pk>/',MCQDetailView.as_view(), name = 'mcq-detail'),
    path('mcq/create/',MCQCreateView.as_view(), name = 'mcq-create'),
    path('mcq/<int:pk>/update/', MCQUpdateView.as_view(), name = 'mcq-update'),
    path('mcq/<int:pk>/delete/', MCQDeleteView.as_view(), name = 'mcq-delete'),
    path('tof/<int:pk>/',TOFDetailView.as_view(), name = 'tof-detail'),
    path('tof/create/',TOFCreateView.as_view(), name = 'tof-create'),
    path('tof/<int:pk>/update/', TOFUpdateView.as_view(), name = 'tof-update'),
    path('tof/<int:pk>/delete/', TOFDeleteView.as_view(), name = 'tof-delete'),
    path('identification/<int:pk>/',IdentificationDetailView.as_view(), name = 'identification-detail'),
    path('identification/create/',IdentificationCreateView.as_view(), name = 'identification-create'),
    path('identification/<int:pk>/update/', IdentificationUpdateView.as_view(), name = 'identification-update'),
    path('identification/<int:pk>/delete/', IdentificationDeleteView.as_view(), name = 'identification-delete'),

]
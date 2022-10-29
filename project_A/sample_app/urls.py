from django.urls import path
from .views import (
    DataListView,
    DataDetailView,
    DataCreateView,
)
from . import views

urlpatterns = [
    path('', DataListView.as_view(), name = 'sample_app-home'),
    path('data/<int:pk>/', DataDetailView.as_view(), name = 'data-detail'),
    path('data/new/', DataCreateView.as_view(), name = 'data-create'),
    path('about/', views.about, name = 'sample_app-about'),
]
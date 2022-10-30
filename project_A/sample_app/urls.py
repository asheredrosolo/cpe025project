from django.urls import path
from .views import (
    DataListView,
    DataDetailView,
    DataCreateView,
    DataUpdateView,
    DataDeleteView,
    UserDataListView,
)
from . import views

urlpatterns = [
    path('', DataListView.as_view(), name = 'sample_app-home'),
    path('user/<str:username>/', UserDataListView.as_view(), name = 'user-data'),
    path('data/<int:pk>/', DataDetailView.as_view(), name = 'data-detail'),
    path('data/new/', DataCreateView.as_view(), name = 'data-create'),
    path('data/<int:pk>/update/', DataUpdateView.as_view(), name = 'data-update'),
    path('data/<int:pk>/delete/', DataDeleteView.as_view(), name = 'data-delete'),
    path('about/', views.about, name = 'sample_app-about'),
]
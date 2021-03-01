from django.urls import path
from .views import ThreadListView, ThreadDetailView
from . import views


urlpatterns = [
    path('', ThreadListView.as_view(), name='index'),
    path('<int:pk>/', ThreadDetailView.as_view(), name='detail'),
    path('add/', views.add_thread, name='add')
]

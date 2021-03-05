from django.urls import path
from .views import ThreadListView, ThreadDetailView, OneUserThreadsView
from . import views


urlpatterns = [
    path('', ThreadListView.as_view(), name='index'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='detail'),
    path('user/<str:username>/threads/', OneUserThreadsView.as_view(), name='one-threads-list'),
    path('add/', views.add_thread, name='add')
]

from django.urls import path
from .views import ThreadListView, ThreadDetailView, OnesThreadsView
from . import views


urlpatterns = [
    path('', ThreadListView.as_view(), name='index'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='detail'),
    path('user/<str:username>/threads/', OnesThreadsView.as_view(), name='ones_threads_list'),
    path('add/', views.add_thread, name='add'),
    path('all-threads/', views.AllThreadListView.as_view(), name='all_threads')
]

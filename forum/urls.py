from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:thread_id>/', views.thread_detail, name='detail'),
    path('add/', views.add_thread, name='add')
]

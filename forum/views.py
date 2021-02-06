from django.http import HttpResponse
from .models import ForumThread
from django.shortcuts import render


def index(request):
    # threads = ForumThread.objects.all()
    # context = {
    #     'threads': threads
    # }
    template = 'forum/index.html'
    return render(request, template)


def thread_detail(request, thread_id):
    return HttpResponse(f"this is thread number {thread_id}")

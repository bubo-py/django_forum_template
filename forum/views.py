from django.http import HttpResponse
from .models import ForumThread
from django.shortcuts import render, get_object_or_404


def index(request):
    # threads = ForumThread.objects.all()
    # context = {
    #     'threads': threads
    # }
    template = 'forum/index.html'
    return render(request, template)


def thread_detail(request, thread_id):
    thread = get_object_or_404(ForumThread, pk=thread_id)
    return render(request, 'forum/thread_detail.html', {'thread': thread})

from django.http import HttpResponse
# from .models import ForumThread


def index(request):
    return HttpResponse("it's an index page")


def thread_detail(request, thread_id):
    return HttpResponse(f"this is thread number {thread_id}")

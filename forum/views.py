from django.http import HttpResponse


def index(request):
    return HttpResponse("it's an index page")

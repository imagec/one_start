from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def get_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
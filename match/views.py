from django.http import HttpResponse

# Created views here.

def index(request):
	return HttpResponse("Cricket Match Database - RDBMS Project")
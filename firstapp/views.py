from django.shortcuts import HttpResponse 
from django.shortcuts import render
from django.shortcuts import redirect
import datetime,json
from firstapp.models import Usermodel


 
def index(request):
    return HttpResponse("<p>Hello Yudhbir</p>")
	
def get_time(request):
	now = datetime.datetime.now()
	html = "<html><body>Current date and time: "+format(now)+"</body></html>"
	return HttpResponse(html)
	
def template_view(request):
	now = datetime.datetime.now()
	return render(request, 'firstapp/datetime.html', {'now': now})
	
def userlist(request):
	objects = Usermodel.objects.values().order_by('id')	
	return render(request, 'firstapp/datetime.html', {'objects': objects})
	# return HttpResponse(objects)
	
	
	
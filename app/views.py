from django.shortcuts import render
from .tasks import sending_data
# Create your views here.

def index(request):
	context = {}
	sending_data()
	return render(request,"app/index.html",context)



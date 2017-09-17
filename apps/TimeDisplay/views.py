from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  'currentdatetime': strftime("%Y-%m-%d %H:%M %P", gmtime())
  }
  return render(request, 'TimeDisplay/index.html', context)

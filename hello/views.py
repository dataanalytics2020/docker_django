from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 'name':'anri'}
    return render(request,'hello/index.html',context)

def home(request):

    return render(request,'hello/home.html',context)

def info(request):
    return render(request,'hello/info.html',context)
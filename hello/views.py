from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 'name':'anri'}
    return render(request,'hello/index.html',context)

def about(request):
    return render(request,'hello/about.html')

def info(request):
    return render(request,'hello/info.html')
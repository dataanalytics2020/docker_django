from django.shortcuts import render

# Create your views here.
def index(request):
    context = { 'name':'anri'}
    return render(request,'hello/index.html',context)
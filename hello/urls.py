from django.urls import path,include
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index,name='index')

]
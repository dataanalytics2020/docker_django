from django.urls import path,include
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index,name='index'),
    path('home', views.home,name='home'),
    path('info', views.info,name='info')

]
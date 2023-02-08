from django.urls import path,include
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('info', views.info,name='info'),

]
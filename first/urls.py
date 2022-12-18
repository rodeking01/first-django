from django.urls import path
from . import views

urlpatterns = [
    # ex: /first/
    path('', views.index, name='index'),
    # ex: /first/select/
    path('select/', views.select, name='select'),
    # ex: /first/result
    path('result/', views.result, name='result'),
    ]
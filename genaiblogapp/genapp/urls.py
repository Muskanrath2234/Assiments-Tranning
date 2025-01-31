from django.urls import path
from .views import *
urlpatterns = [
    path('', Blog_Generator_View,name='Blog_Generator_View')
]


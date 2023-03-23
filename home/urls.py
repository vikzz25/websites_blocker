from django.urls import path, include
from home import views
from .views import *


urlpatterns = [
    path('',views.index,name="home"),
    path('About',views.About,name="home"),
    path('block',views.block,name="home"),
]
from django.urls import path, include
from home import views
from .views import *


urlpatterns = [
    path('',views.index,name="home"),
    #path('',views.index,name=""),
    path('About',views.About,name="home"),
    path('register',views.register,name="home"),
    path('block',views.block,name="home"),
    path('unblock',views.unblock,name="home"),
    path('options',views.options,name="home"),
    path('block_entry',views.block_entry,name="home"),
    path('unblock_entry',views.unblock_entry,name="home"),
    path('Login',views.login_user,name="home"),
    path('logoutuser', views.logout_user, name='home'),
    path('step', views.step, name='home'),
    path('contact', views.contact, name='home')
]
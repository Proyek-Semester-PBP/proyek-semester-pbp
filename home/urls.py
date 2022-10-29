from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('home/', show_home_loggedin, name='show_home_loggedin'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
]
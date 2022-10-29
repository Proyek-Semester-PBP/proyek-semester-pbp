from django.urls import path
from home.views import show_homepage, login_user, register, logout_user

app_name = 'home'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('login/', login_user, name='login_user'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout_user'),
]
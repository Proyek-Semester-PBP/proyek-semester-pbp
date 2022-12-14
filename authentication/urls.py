from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('update/', show_profile, name = 'update_profile'),
    path('register/', register, name = "register"),
    path('addpoints/', addPoint, name = "addPoints")
]
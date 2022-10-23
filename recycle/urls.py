from django.urls import path
from recycle.views import show_recycle

app_name = 'recycle'

urlpatterns = [
    path('', show_recycle, name='show_recycle'),
]
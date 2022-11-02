from django.urls import path
from recycle.views import add_history, show_recycle, show_json, create_dropoff, create_pickup, show_dumb

app_name = 'recycle'

urlpatterns = [
    path('dumb/', show_dumb, name='show_dumb'),
    path('', show_recycle, name='show_recycle'),
    path('pickup/', create_pickup, name='create_pickup'),
    path('dropoff/', create_dropoff, name='create_dropoff'),
    path('json/', show_json, name='show_json'),
    path('add_history/', add_history, name='add_history'),
]

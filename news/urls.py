from django.urls import path
from news.views import show_news
from news.views import show_json
from news.views import show_json_by_id

app_name = 'news'

urlpatterns = [
    path('', show_news, name='show_news'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]
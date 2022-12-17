from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('update/', show_profile, name = 'update_profile'),
    path('register/', register, name = "register"),
    path('addpoints/', addPoint, name = "addPoints"),
    path('add_history_flutter/', add_history_flutter, name = "addHistory"),
    path('redeem/', redeem, name = "redeem"),
    path('post_review/', post_review, name = "post_review"),
    path('show_bookmarks/', show_bookmarks, name='show_bookmarks'),
    path('bookmark/<int:id>', bookmark_item, name='bookmark_item'),
    path('remove_bookmark/<int:id>', remove_bookmark, name='remove_bookmark'),
]
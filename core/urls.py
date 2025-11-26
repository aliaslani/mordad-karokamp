from django.urls import path
from core.views import user_list, jadid


urlpatterns = [
    path("", jadid, name="home"),
    path("posts/", jadid, name="posts"),
    path("users/", user_list, name="users"),
]

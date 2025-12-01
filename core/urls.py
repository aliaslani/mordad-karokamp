from django.urls import path
from core.views import user_list, jadid, post_detail, new_post


urlpatterns = [
    path("", jadid, name="home"),
    path("users/", user_list, name="users"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
    path("post/new/", new_post, name="new_post"),
]

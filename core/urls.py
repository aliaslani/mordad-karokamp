from django.urls import path
from core.forms import EditPostForm
from core.views import (
    user_list,
    jadid,
    post_detail,
    new_post,
    edit_post,
    delete_post,
)


urlpatterns = [
    path("", jadid, name="home"),
    path("users/", user_list, name="users"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
    path("post/new/", new_post, name="new_post"),
    path("post/delete/<int:post_id>/", delete_post, name="delete_post"),
    path("post/edit/<int:post_id>/", edit_post, name="edit_post"),
]

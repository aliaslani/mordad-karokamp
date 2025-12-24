from django.contrib import admin
from core.models import Post, Like
from django.urls import reverse
from django.utils.html import format_html

admin.site.register(Like)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "user_link",
        "visible",
        "created_at",
        "has_image",
    ]

    list_display_links = ["id", "title"]

    list_filter = ["user", "visible", "is_deleted", "created_at"]
    search_fields = ["title", "content"]

    @admin.display(description="User", ordering="user")
    def user_link(self, obj):
        if not obj.user:
            return "-"

        url = reverse(
            "admin:%s_%s_change"
            % (obj.user._meta.app_label, obj.user._meta.model_name),
            args=[obj.user.pk],
        )

        return format_html('<a href="{}">{}</a>', url, obj.user)

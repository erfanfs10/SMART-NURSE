from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):

    list_display = ("username", "email", "phone_number", "first_name", "last_name",
                     "birthday", "gender", "access", "is_active", "created")
    list_filter = ("gender", "is_active")
    list_editable = ("is_active",)

    fieldsets = [
        (
            None, 
            {"fields": ["username", "email", "phone_number", "first_name", "last_name",
                     "birthday", "gender", "access", "language", "theme", "about", 
                     "avatar", "is_active", "password"]
            }
        ),
        (
            "Permissions",
            {"fields": ["is_staff", "is_superuser"]
            }
        ),
    ]

    ordering = ["created"]

admin.site.register(User, UserAdmin)

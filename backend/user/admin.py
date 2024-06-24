from django.contrib import admin

from user.models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "roll",
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "gender",
        "marital_status",
        "nationality",
        "address",
        "session",
        "department",
        "is_student",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
        "password",
    )
    list_display_links = (
        "username",
        "phone_number",
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "username",
        "phone_number",
        "email",
    )
    list_per_page = 25


admin.site.register(UserAccount, UserAccountAdmin)

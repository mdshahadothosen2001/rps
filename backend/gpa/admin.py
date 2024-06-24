from django.contrib import admin

from .models import GPA


class GPAAdmin(admin.ModelAdmin):
    def display_student(self, obj):
        return obj.student.username
    
    def display_semester(self, obj):
        return obj.semester.semester_no

    
    list_display = (
        "id",
        "display_student",
        "display_semester",
        "point",
    )
    list_display_links = (
        "display_student",
        "point",
    )
    search_fields = (
        "student",
    )
    list_per_page = 25


admin.site.register(GPA, GPAAdmin)

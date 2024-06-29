from django.contrib import admin

from .models import Mark


class MarkAdmin(admin.ModelAdmin):
    def display_session(self, obj):
        return obj.examination.semester.session
    
    def display_semester(self, obj):
        return f"{obj.examination.semester.semester_no} {obj.examination.semester.session}"
    
    def display_examination(self, obj):
        return f"{obj.examination.name} {obj.examination.course}"
    
    def display_student(self, obj):
        return obj.student.username

    
    list_display = (
        "id",
        "display_examination",
        "display_session",
        "display_semester",
        "display_student",
        "mark",
    )
    list_display_links = (
        "display_examination",
        "display_student",
    )
    search_fields = (
        "examination",
    )
    list_per_page = 25


admin.site.register(Mark, MarkAdmin)

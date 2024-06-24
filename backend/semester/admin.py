from django.contrib import admin

from .models import Semester


class SemesterAdmin(admin.ModelAdmin):
    def display_teachers(self, obj):
        return ", ".join([teacher.username for teacher in obj.teachers.all()])
    
    def display_students(self, obj):
        return ", ".join([student.username for student in obj.students.all()])
    
    list_display = (
        "id",
        "semester_no",
        "session",
        "department",
        "display_teachers",
        "display_students",
        "courses",
        "total_courses",
        "is_active",
    )
    list_display_links = (
        "semester_no",
        "session",
        "department",
    )
    search_fields = (
        "semester_no",
        "session",
        "department",
    )
    list_per_page = 25


admin.site.register(Semester, SemesterAdmin)

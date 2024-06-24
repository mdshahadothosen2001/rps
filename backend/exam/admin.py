from django.contrib import admin

from django.utils.html import mark_safe

from .models import Examination


class ExaminationAdmin(admin.ModelAdmin):
    def display_teacher(self, obj):
        return obj.teacher.username
    
    def display_semester(self, obj):
        return obj.semester.semester_no
    
    def display_question(self, obj):
        return mark_safe('<img src="%s" style="max-width:100px; max-height:100px;" />' % obj.question)
    display_question.allow_tags = True
    display_question.short_description = 'question'

    
    list_display = (
        "id",
        "name",
        "course",
        "display_teacher",
        "display_semester",
        "display_question",
        "deadline",
    )
    list_display_links = (
        "name",
        "deadline",
    )
    search_fields = (
        "name",
        "deadline",
    )
    list_per_page = 25


admin.site.register(Examination, ExaminationAdmin)

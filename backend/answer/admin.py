from django.contrib import admin

from django.utils.html import mark_safe

from .models import Answer


class AnswerAdmin(admin.ModelAdmin):
    def display_session(self, obj):
        return obj.examination.semester.session
    
    def display_semester(self, obj):
        return obj.examination.semester.semester_no
    
    def display_examination(self, obj):
        return obj.examination.name
    
    def display_student(self, obj):
        return obj.student.username
    
    def display_answer(self, obj):
        return mark_safe('<img src="%s" style="max-width:100px; max-height:100px;" />' % obj.answer)
    display_answer.allow_tags = True
    display_answer.short_description = 'answer'

    
    list_display = (
        "id",
        "display_examination",
        "display_session",
        "display_semester",
        "display_student",
        "display_answer",
    )
    list_display_links = (
        "display_examination",
        "display_student",
    )
    search_fields = (
        "examination",
    )
    list_per_page = 25


admin.site.register(Answer, AnswerAdmin)

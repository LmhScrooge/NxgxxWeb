from django.contrib import admin
from .models import Question,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QustionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    inlines = [ChoiceInline]
admin.site.register(Question,QustionAdmin)
admin.site.register(Choice)
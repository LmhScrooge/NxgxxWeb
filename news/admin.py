from django.contrib import admin
from .models import Article,Column
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time','published','author',)
    search_fields = ['title', 'column','published',]
    list_filter = ('column',)
    filter_vertical = ['column']

    class Media:
        js = ('/static/js/KindEditor/kindeditor-all-min.js',
              '/static/js/KindEditor/lang/zh-CN.js',
              '/static/js/KindEditor/config.js')
admin.site.register(Article,ArticleAdmin)
admin.site.register(Column)
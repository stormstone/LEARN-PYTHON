from django.contrib import admin

from models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)


# Register your models here.
admin.site.register(Article, ArticleAdmin)

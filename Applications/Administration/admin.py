from django.contrib import admin
from .models import TypesPublication, Article, Publication, Denounce


class TypesPublicationAdmin(admin.ModelAdmin):
    list_display = ('name','is_active','creationTime')
    search_fields = ('name', 'creationTime')
    empty_value_display = 'Not Declared'
    date_hierarchy = 'creationTime'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','startOfRegistration','endOfRegistration','is_active','creationTime')
    search_fields = ('title', 'creationTime')
    list_filter = ('typeOfNotice', 'is_active')
    empty_value_display = 'Not Declared'
    date_hierarchy = 'creationTime'

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title','is_active','creationTime')
    search_fields = ('title', 'creationTime')
    list_filter = ['is_active']
    empty_value_display = 'Not Declared'
    date_hierarchy = 'creationTime'

class DenounceAdmin(admin.ModelAdmin):
    list_display = ('name','descreption','creationTime')
    search_fields = ('name', 'descreption')
    empty_value_display = 'Not Declared'
    date_hierarchy = 'creationTime'

admin.site.register(TypesPublication, TypesPublicationAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Denounce, DenounceAdmin)
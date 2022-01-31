from django.contrib import admin
from .models import LikePublication, DeslikePublication, LikeArticle, DeslikeArticle, DenouncePublication, DenounceArticle


class DenouncePublicationAdmin(admin.ModelAdmin):
    list_display = ('publication','justification','user','creationTime')
    search_fields = ('name', 'creationTime')
    empty_value_display = 'Not Declared'
    date_hierarchy = 'creationTime'

class DenounceArticleAdmin(admin.ModelAdmin):
    list_display = ('publication','justification','user','creationTime')
    search_fields = ('name', 'creationTime')
    empty_value_display = 'Not Declared'
    date_hierarchy = 'creationTime'

admin.site.register(LikePublication)
admin.site.register(DeslikePublication)
admin.site.register(LikeArticle)
admin.site.register(DeslikeArticle)
admin.site.register(DenouncePublication, DenouncePublicationAdmin)
admin.site.register(DenounceArticle, DenounceArticleAdmin)

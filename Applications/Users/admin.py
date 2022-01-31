from django.contrib import admin
from .models import Continent, Country, State, City, Area, SubArea, User

# ACRESCENTAR SOMENTE VIZUALIZAÇÕES

class ContinentAdmin(admin.ModelAdmin):
    list_display = ('name', 'creationTime')
    search_fields = ('name', 'creationTime')
    empty_value_display = 'Not Declared'
    date_hierarchy = 'creationTime'

class CountryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('titulo', )}
    list_display = ('descreption','continent','creationTime') 
    empty_value_display = 'Not Declared'
    list_filter = ['continent']
    date_hierarchy = 'creationTime'
    search_fields = ['descreption']
    view_on_site = False

class StateAdmin(admin.ModelAdmin):
    list_display = ('descreption','country','creationTime') 
    empty_value_display = 'Not Declared'
    list_filter = ['country']
    date_hierarchy = 'creationTime'
    search_fields = ['descreption']
    view_on_site = False

class CityAdmin(admin.ModelAdmin):
    list_display = ('descreption','state','creationTime') 
    empty_value_display = 'Not Declared'
    list_filter = ['state']
    date_hierarchy = 'creationTime'
    search_fields = ['descreption']
    view_on_site = False

class AreaAdmin(admin.ModelAdmin):
    list_display = ('nameArea','creationTime') 
    empty_value_display = 'Not Declared'
    date_hierarchy = 'creationTime'
    search_fields = ['nameArea']
    view_on_site = False

class SubAreaAdmin(admin.ModelAdmin):
    list_display = ('name','area','creationTime') 
    empty_value_display = 'Not Declared'
    list_filter = ['area']
    date_hierarchy = 'creationTime'
    search_fields = ['area']
    view_on_site = False

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','state','idGroup','creationTime') 
    empty_value_display = 'Not Declared'
    list_filter = ('profile', 'is_active', 'is_staff', 'is_superuser')
    date_hierarchy = 'creationTime'
    search_fields = ['name']
    view_on_site = False


admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(SubArea,SubAreaAdmin)
admin.site.register(User, UserAdmin)

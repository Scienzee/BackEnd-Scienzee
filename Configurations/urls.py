from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluindo rotas de outras urls
    path('', include('Users.urls')),
    path('Administration', include('Administration.urls')),    
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

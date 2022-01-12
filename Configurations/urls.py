from django.contrib import admin
from django.urls import path, include
# from Users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluindo rotas de outras urls
    path('', include('Users.urls')),
    path('Administration', include('Administration.urls')),
    # path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    # path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),

    
]

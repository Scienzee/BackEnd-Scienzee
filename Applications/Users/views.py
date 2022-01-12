from django.shortcuts import render

# Importando o diretório onde ficará as Views 
from Administration.Views import News
from Administration.Views import Notice
from Administration.Views import Articles

# Importando o login de Social Media
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter
# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
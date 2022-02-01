from rest_framework import serializers
from .models import User

# TRADUÇÃO DJANGO
# https://github.com/marinho/aprendendo-django/blob/master/22-o-mesmo-site-em-varios-idiomas.md


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_field = ['is_active', 'is_staff', 'is_superuser', 'creationTime', 'deactivationTime']

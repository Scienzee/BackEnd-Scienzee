from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['is_active', 'is_staff', 'is_superuser']
        # read_only_field = ['is_active', 'created', 'updated']

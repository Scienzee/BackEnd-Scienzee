from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from base.api.serializers import *
from base.models import *

class CountryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
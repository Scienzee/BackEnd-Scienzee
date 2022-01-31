from rest_framework import serializers
from .models import TypesPublication, Article, Publication, Denounce



class TypesPublicationSerializer(serializers.ModelSerializer):

    """
        Construíndo o seralizer do models LikePublication, transformando os objetos em JSON
    """

    class Meta:
        model = TypesPublication
        fields = ['name', 'descreption', 'icons', 'creationTime', 'is_active']


class ArticleSerializer(serializers.ModelSerializer):

    """
        Construíndo o seralizer do models Article, transformando os objetos em JSON
    """

    class Meta:
        model = Article
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):

    """
        Construíndo o seralizer do models Publication, transformando os objetos em JSON
    """

    class Meta:
        model = Publication
        fields = '__all__'
        

class DenounceSerializer(serializers.ModelSerializer):

    """
        Transformando os dados(Objetos) dessa classe em JSON
    """

    class Meta:
        model = Denounce
        fields = ('name', 'descreption', 'creationTime')
from rest_framework import serializers
from .models import LikePublication, DeslikePublication, LikeArticle, DeslikeArticle, DenouncePublication, DenounceArticle


class LikePublicationSerializer(serializers.ModelSerializer):

    """
        Construíndo o seralizer do models LikePublication, transformando os objetos en JSON
    """

    class Meta:
        model = LikePublication
        fields = ('publication', 'user', 'creationTime')


class DeslikePublicationSerializer(serializers.ModelSerializer):

    """
        Construíndo o seralizer do models DeslikePublication, transformando os objetos en JSON
    """

    class Meta:
        model = DeslikePublication
        fields = ('publication', 'user', 'creationTime')


class LikeArticleSerializer(serializers.ModelSerializer):

    """
        Construíndo o seralizer do models LikeArticle, transformando os objetos en JSON
    """

    class Meta:
        model = LikeArticle
        fields = ('publication', 'user', 'creationTime')


class DeslikeArticleSerializer(serializers.ModelSerializer):

    """
        Construíndo o seralizer do models DeslikeArticle, transformando os objetos en JSON
    """

    class Meta:
        model = DeslikeArticle
        fields = ('publication', 'user', 'creationTime')


class DenouncePublicationSerializer(serializers.ModelSerializer):

    """
        Construíndo o seralizer do models DenouncePublication, transformando os objetos en JSON
    """

    class Meta:
        model = DenouncePublication
        fields = ('publication', 'user', 'creationTime')


class DenounceArticleSerializer(serializers.ModelSerializer):

    """
        Construíndo o seralizer do models DenounceArticle, transformando os objetos en JSON
    """

    class Meta:
        model = DenounceArticle
        fields = ('publication', 'user', 'creationTime')
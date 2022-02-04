from django.db import models
from django.db.models.deletion import CASCADE
import logging

"""
Models para gestão de dados base, comuns a outras classes
"""

class Country(models.Model):
    descreption = models.CharField("Descreption of the state", max_length=100)
    initials = models.CharField("Initials of the state ", max_length=100)
    creation_time = models.DateTimeField("Creation Time", auto_now_add=True)
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural="Countrys"
        ordering = ['descreption']
        app_label = 'base'

    def __str__(self):
        return f'{self.descreption} -- {self.initials}'
        
    def __repr__(self):
        return f'[ ModelsCountry ] descreption = {self.descreption}'

    def crete_register(descreption, initials):
        register = Country()
        register.descreption = descreption
        register.initials = initials
        try:
            register.save()
            logging.info('** Registro inserido da tabela "Coutry" **')
        except Exception as ex:
            logging.warning('** Não conseguiu inserir o registro na tabela "Coutry" **')

    def get_all():
        return Country.objects.all()
    

class State(models.Model):
    country = models.ForeignKey(Country, related_name="CountryOfTheState", on_delete=models.CASCADE)
    descreption = models.CharField("Descreption of the state", max_length=100)
    initials = models.CharField("Initials of the state ", max_length=100)
    creation_time = models.DateTimeField("Creation Time", auto_now_add=True)
    
    class Meta:
        verbose_name = "State"
        verbose_name_plural="States"
        ordering = ['descreption']
        app_label = 'base'

    def __str__(self):
        return self.descreption


class City(models.Model):
    descreption = models.CharField("Descreption of the City", max_length=100)
    state = models.ForeignKey(State, related_name="StateOfCity", max_length=100, on_delete=CASCADE)
    creation_time = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural="Citys"
        ordering = ['descreption']
        app_label = 'base'

    def __str__(self):
        return self.descreption

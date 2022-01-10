from django.db import models
from Users import User, State, Country, Area, AreaOfThePrerence

class TypesPublication(models.Model):
    name = models.CharField("Publication type name", max_length=20)
    descreption = models.CharField("Descreption of the types", max_length="100")
    icone =  models.CharField("Icons of the Types", max_length="100")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    is_active = models.BooleanField("Type is active", default=1)
    disabledBy = models.ForeignKey("Users.User", related_name="disabledByUser", null=True, blank=True)
    deactivationTime = models.DateTimeField("Deactivation Time", auto_now_add=False, null=True, blank=True)


    class Meta:
        verbose_name="User"
        verbose_name_plural="Users"
        ordering = ['name']
        app_label = "Users"

    def __str__(self):
        return self.name

class Notice(models.Model):

    TYPE_NOTICE = [
        ("PE", "Pré-edital"),
        ("AB", "Aberto"),
        ("FC", "Fechado"),
        ("TD", "Todos"),
    ]

    title = models.CharField("Title of Notice", max_length=150)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    descreption = models.CharField("Descreption of the", max_length=250)
    startOfRegistration = models.DateTimeField("start registration", auto_now_add=False)
    endOfRegistration = models.DateTimeField("End of Registration", auto_now_add=False)
    country = models.ManyToManyField(Country)
    states = models.ManyToManyField(State)
    city = models.ManyToManyField(City)
    typeOfNotice = models.CharField('Type of the notice', max_length=2, choices=TYPE_NOTICE, blank=True, null=True)
    area = models.ManyToManyField(Area)    
    subArea = models.ManyToManyField(AreaOfThePrerence)





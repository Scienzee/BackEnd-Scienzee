from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.deletion import CASCADE
from base.models import *
from django.utils import timezone
from dev.models import Dev


class UserManager(BaseUserManager):
    def _create_user(self, name, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not name:
            return None
        email = self.normalize_email(email)
        
        user = self.model(
            name=name, 
            email=email, 
            is_staff=is_staff, 
            is_active=True, 
            is_superuser=is_superuser, 
            last_login=now, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, name, email=None, password=None, **extra_fields):
        return self._create_user(name, email, password, False, False, **extra_fields)
    
    def create_superuser(self, name, email, password, **extra_fields):
        if not Dev.objects.filter(email=email):
            logging.info('** O email informado não consta na lista de DEVS **')
            return None
        user=self._create_user(name, email, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user


class Area(models.Model):
    name_area = models.CharField("Name of the Area", max_length=200)
    creation_time = models.DateTimeField("Creation Time", auto_now_add=True)
    
    class Meta:
        verbose_name="Area"
        verbose_name_plural="Areas"
        ordering = ['name_area']
        app_label = 'user'

    def create_area(name_area):
        register = Area()
        register.name_area = name_area
        try:
            register.save()
            logging.info('** Novo Usuário SUPER cadastrado **')
            return register
        except Exception as ex:
            logging.warning(f'** Não conseguiu cadastrar um registro na tabela "Area" ** | Erro: {ex}')
            None

    def __str__(self):
        return f'[ ModelArea ] name = {self.name}'


class PreferenceArea(models.Model):
    name = models.CharField("Name of preferred area", max_length=100)
    area =  models.ForeignKey(Area,  related_name='AreaOfThePrerence', on_delete=models.CASCADE)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Area Of the Prefence"        
        verbose_name_plural="Area Of the Prefences"
        ordering = ['name']
        app_label = 'user'

    def __str__(self):
        return f'[ ModelPreferenceArea ] name = {self.name}'


class User(AbstractBaseUser,PermissionsMixin):

    ACADEMIC_DEGREE = [
        ("EFI", "Ensino fundamental incompleto"),
        ("EFC", "Ensino fundamental completo"),
        ("EMI", "Ensino médio incompleto"),
        ("EMC", "Ensino médio completo"),
        ("ESI", "Ensino superior incompleto"),
        ("ESC", "Ensino superior completo"),
    ]

    name = models.CharField("Name", max_length = 194, null=True, blank=True)
    birth_date = models.DateField("Birth Date",auto_now=False, auto_now_add=False, null=True, blank=True)
    email = models.EmailField("E-mail",max_length=194, unique=True)
    academic_degree = models.CharField("Academic Degree", max_length=30, choices=ACADEMIC_DEGREE, null=True, blank=True)
    area = models.ManyToManyField(Area)    
    area_preference = models.ManyToManyField(PreferenceArea)
    country =  models.ForeignKey(Country, related_name="ContryOfTheUser", on_delete=models.CASCADE, blank=True  , null=True)
    state = models.ForeignKey(State,on_delete=CASCADE, null=True, blank=True, related_name="StateOfTheUser")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="CityOfTheUser", null=True, blank=True)
    profile_picture = models.ImageField("Profile Picture",  null=True, blank=True, upload_to="ProfilePicture/%y/%m/%d")
    cover_photo = models.ImageField("Cover Photo",  null=True, blank=True, upload_to="CoverPhoto/%y/%m/%d")
    descreption = models.TextField("Descreption", null=True, blank=True)
    creation_time = models.DateTimeField("Creation Time", auto_now_add=True)
    deactivation_time = models.DateTimeField("Deactivation Time", blank=True, null=True)
    is_active = models.BooleanField(verbose_name="User is active ",default=True)
    is_staff  = models.BooleanField(verbose_name="User is staff", default= False)
    is_superuser = models.BooleanField(verbose_name= "User is superuser",default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural="User"
        ordering = ['name']
        app_label = 'user'
        
    def __str__(self):
        return str(self.name)

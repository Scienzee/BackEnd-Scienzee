from django.db import models
from django.contrib.auth.models import( BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.db.models.deletion import CASCADE, SET_NULL
from smart_selects.db_fields import ChainedForeignKey


ACADEMIC_DEGREE = [
    ("EFI", "Ensino fundamental incompleto"),
    ("EFC", "Ensino fundamental completo"),
    ("EMI", "Ensino médio incompleto"),
    ("EMC", "Ensino médio completo"),
    ("ESI", "Ensino superior incompleto"),
    ("ESC", "Ensino superior completo"),
]

class UsuarioManager(BaseUserManager):
    def create_user(self,email,password=None):
        usuario = self.model(email = email)
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)        
        usuario.save()
        
        return usuario
    
    def create_superuser(self,email,password):
        usuario = self.create_user(email = email, password = password)
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()
        return usuario

class State(models.Model):
    descreption = models.CharField("Descreption of the state", max_length=100)
    initials = models.CharField("Initials of the state ", max_length=100)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    
    class Meta:
        verbose_name = "State"
        verbose_name_plural="States"
        ordering = ['descreption']
        app_label = 'Users'

    def __str__(self):
        return self.descreption

class City(models.Model):
    descreption = models.CharField("Descreption of the City", max_length=100)
    estado = models.ForeignKey(State, related_name="StateOfCity" max_length=100, on_delete=CASCADE)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural="Citys"
        ordering = ['descreption']
        app_label = 'Users'


    def __str__(self):
        return self.descreption

class Area(models.Model):
    nameArea = models.CharField("Name of the Area", max_length=200)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    
    class Meta:
        verbose_name="Area"
        verbose_name_plural="Areas"
        ordering = ['nameArea']
        app_label = 'Users'

class PreferenceArea(models.Model):
    name = models.CharField("Name of preferred area", max_length=100)
    area =  models.ForeignKey(Area,  related_name='AreaOfThePrerence', on_delete=models.CASCADE)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Area Of the Prefence"
        verbose_name_plural="Area Of the Prefences"
        ordering = ['name']
        app_label = 'Users'

    def __str__(self):
        return str(self.name)


class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField("Name", max_length = 194, null=True, blank=True)
    birthDate = models.DateField("Birth Date",auto_now=False, auto_now_add=False, null=True, blank=True)
    email = models.EmailField("E-mail",max_length=194, unique=True)
    AcademicDegree = models.CharField("Academic Degree", max_length=30, choices=ESCOLARIDADE, null=True, blank=True)
    areaPreference = models.ManyToManyField(AreaAtuacao)
    state = models.ForeignKey("State",on_delete=CASCADE ,null=True, blank=True)
    city = ChainedForeignKey(City, 
        chained_field="state", 
        chained_model_field="state"
        show_all=False,
        auto_choose=True,
        sort=True        
    )
    profilePicture = models.ImageField("Profile Picture",  null=True, blank=True, upload_to="ProfilePicture/%y/%m/%d")
    coverPhoto = models.ImageField("Cover Photo",  null=True, blank=True, upload_to="CoverPhoto/%y/%m/%d")
    descreption = models.TextField("Descreption", null=True, blank=True)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    deactivationTime = models.DateTimeField("Deactivation Time", blank=True, null=True)
    is_active = models.BooleanField(verbose_name="User is active ",default=True)
    is_staff  = models.BooleanField(verbose_name="User is staff", default= False)
    is_superuser = models.BooleanField(verbose_name= "User is superuser",default=False)

    USERNAME_FIELD = "email"
    objects = UsuarioManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural="User"
        ordering = ['name']
        app_label = 'Users'
        
    def __str__(self):
        return str(self.name)

    # def get_full_name(self): 
    #     return str(self.nome + ' ' + self.sobrenome)

# class FavoritosUsuarios(models.Model):
#     usuario = models.ForeignKey("Usuario", on_delete=CASCADE, related_name="FavoritosdoUsuario")
#     publicacao = models.ForeignKey("Publicacoes.Publicacao", on_delete=CASCADE, related_name="PublicacoesFavoritas")
#     dataFavoritad = models.DateTimeField("Data da favoritação", auto_now_add=True)

#     class Meta:
#         verbose_name = "Favoritos Usuarios"
#         verbose_name_plural="Favoritos Usuarios"
#         ordering = ['usuario']
#         app_label = 'Usuarios'
        
#     def __str__(self):
#         return str(self.usuario)
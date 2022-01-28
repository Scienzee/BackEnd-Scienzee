from django.db import models
from django.contrib.auth.models import( BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.encoding import force_str


class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        user = self.model(email = email)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False

        if password:
            user.set_password(password)        
        user.save()
        
        return usuario
    
    def create_superuser(self,email,password):
        user = self.create_user(email = email, password = password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user

class Continent(models.Model):
    
    """
        Continent existentes na atualidade, para facilitar na hora da busca pelo país
    """

    name = models.CharField("Name of the Continent", max_length=50)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Continent"
        verbose_name_plural="Continent"
        ordering = ['name']
        app_label = 'Users'

    def __str__(self):
        return self.descreption

class Country(models.Model):
    
    """
        Países existentes na atualidade. Entretanto no Front-End deverá ser mostrado somente os países de acordo com 
        o continente selecionado
    """

    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name="ContintOfTheCountry")
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

class State(models.Model):

    """
        Estados existentes na atualidade. Entretanto no Front-End deverá ser mostrado somente os estados de acordo com 
        o país selecionado
    """

    country = models.ForeignKey(Country, related_name="CountryOfTheState", on_delete=models.CASCADE)
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

    """
        Cidades existentes na atualidade. Entretanto no Front-End deverá ser mostrado somente as cidades de acordo com 
        o estado selecionado
    """

    descreption = models.CharField("Descreption of the City", max_length=100)
    state = models.ForeignKey(State, related_name="StateOfCity", max_length=100, on_delete=CASCADE)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural="Citys"
        ordering = ['descreption']
        app_label = 'Users'


    def __str__(self):
        return self.descreption

class Area(models.Model):

    """
        Grandes áreas como Ciencias exatas e da terra, engenharias, ciencias humanas etc..
    """

    nameArea = models.CharField("Name of the Area", max_length=200)
    image =  models.ImageField("Image of the Area", upload_to="ImageArea/%y/%m/%d")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    
    class Meta:
        verbose_name="Area"
        verbose_name_plural="Areas"
        ordering = ['nameArea']
        app_label = 'Users'

class SubArea(models.Model):

    """
        Pequenas áreas como Álgebra, Probalidade, Analise etc...
        Ela precisa ser selecionada de acordo com a area escolhida
    """

    name = models.CharField("Name of preferred area", max_length=100)
    image =  models.ImageField("Image of the Area", upload_to="SubArea/%y/%m/%d")
    area =  models.ForeignKey(Area,  related_name='AreaOfThePrerence', on_delete=models.CASCADE)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Sub Area"        
        verbose_name_plural="Sub Areas"
        ordering = ['name']
        app_label = 'Users'

    def __str__(self):
        return str(self.name)


class User(AbstractBaseUser,PermissionsMixin):

    """
        Usuários dos sistemas Usuário Físico e Usuário Jurídico
    """

    ACADEMIC_DEGREE = [
        ("EFI", "Ensino fundamental incompleto"),
        ("EFC", "Ensino fundamental completo"),
        ("EMI", "Ensino médio incompleto"),
        ("EMC", "Ensino médio completo"),
        ("ESI", "Ensino superior incompleto"),
        ("ESC", "Ensino superior completo"),
    ]

    PROFILE = [
        ("F","Físico"),
        ("J","Jurídico"),
    ]

    profile = models.CharField("Profile of the User", max_length = 194, null=True, blank=True, choices=PROFILE)
    name = models.CharField("Name", max_length = 194, null=True, blank=True)
    birthDate = models.DateField("Birth Date",auto_now=False, auto_now_add=False, null=True, blank=True)
    email = models.EmailField("E-mail",max_length=194, unique=True)
    Cnpj = models.CharField("CNPJ", max_length=20, unique=True, blank=True, null=True)
    AcademicDegree = models.CharField("Academic Degree", max_length=30, choices=ACADEMIC_DEGREE, null=True, blank=True)
    area = models.ManyToManyField(Area)    
    areaPreference = models.ManyToManyField(SubArea)
    continent = models.ForeignKey(Continent, related_name="ContinentOfTheUser", on_delete=models.PROTECT, null=True, blank=True)
    country =  models.ForeignKey(Country, related_name="ContryOfTheUser", on_delete=models.PROTECT)
    state = models.ForeignKey(State,on_delete=CASCADE, null=True, blank=True, related_name="StateOfTheUser")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="CityOfTheUser", null=True, blank=True)
    profilePicture = models.ImageField("Profile Picture",  null=True, blank=True, upload_to="ProfilePicture/%y/%m/%d")
    coverPhoto = models.ImageField("Cover Photo",  null=True, blank=True, upload_to="CoverPhoto/%y/%m/%d")
    descreption = models.TextField("Descreption", null=True, blank=True)
    idGroup = models.IntegerField(verbose_name = 'Id do grupo', default = 2)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    deactivationTime = models.DateTimeField("Deactivation Time", blank=True, null=True)
    is_active = models.BooleanField(verbose_name="User is active ",default=True)
    is_staff  = models.BooleanField(verbose_name="User is staff", default= False)
    is_superuser = models.BooleanField(verbose_name= "User is superuser",default=False)

    USERNAME_FIELD = "email"
    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural="User"
        ordering = ['name']
        app_label = 'Users'
        
    def __str__(self):
        return str(self.name)



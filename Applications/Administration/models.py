from django.db import models
from Users.models import User, State, Country, Area, PreferenceArea, City

class TypesPublication(models.Model):

    """
        Models para especificar o tipo de publicação por exemplo Artigo, notícia, podcast, curiosidades...
    """

    name = models.CharField("Publication type name", max_length=20)
    descreption = models.CharField("Descreption of the types", max_length=100)
    icone =  models.CharField("Icons of the Types", max_length=100)
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    is_active = models.BooleanField("Type is active", default=1)
    disabledBy = models.ForeignKey("Users.User", related_name="disabledByUser", on_delete=models.CASCADE, null=True, blank=True)
    deactivationTime = models.DateTimeField("Deactivation Time", auto_now_add=False, null=True, blank=True)


    class Meta:
        verbose_name="User"
        verbose_name_plural="Users"
        ordering = ['name']
        app_label = "Users"

    def __str__(self):
        return self.name

class Notice(models.Model):

    """
        Model para criação de Editais!
        Detalhe ainda não consta o atributo de conteúdo, pois preciso estudar com usar nesse caso!
    """

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
    publicationPhoto = models.ImageField("Publication Photo", upload_to="PublicationPhoto/")
    # contentente = RichTextUploadingField("Informações sobre o Edital")
    country = models.ManyToManyField(Country)
    states = models.ManyToManyField(State)
    city = models.ManyToManyField(City)
    typeOfNotice = models.CharField('Type of the notice', max_length=2, choices=TYPE_NOTICE, blank=True, null=True)
    area = models.ManyToManyField(Area)    
    subArea = models.ManyToManyField(PreferenceArea)
    publicationBy = models.ForeignKey("Users.User", on_delete=models.CASCADE, related_name="NoticeBy")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    editedBy = models.ForeignKey("Users.User", on_delete=models.CASCADE, related_name="NoticeEditedBy")
    editDate = models.DateTimeField("Edit Date", auto_now_add=False, null=True, blank=True)    
    is_active = models.BooleanField("Type is active", default=1)
    disabledBy = models.ForeignKey("Users.User", related_name="NoticeDisabledByUser", on_delete=models.CASCADE, null=True, blank=True)
    deactivationTime = models.DateTimeField("Deactivation Time", auto_now_add=False, null=True, blank=True)    

    class Meta:
        verbose_name: "Notice"
        verbose_name_plural =  "Notices"
        ordering =  ["title"]
        app_label =  "Administration"

    def __str__(self):
        return str(self.title)

# class DenounceNotice(models.Model):




class Publication(models.Model):

    """
        Model para criação de publicação como Artigos, Notícias e entre outras categorias que formos criados conforme 
        a nossa necessidade
    """

    title = models.CharField("Title of Notice", max_length=150)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    descreption = models.CharField("Descreption of the", max_length=250)
    publicationPhoto = models.ImageField("Publication Photo", upload_to="PublicationPhoto/")
    typeOfPublication = models.ForeignKey(TypesPublication, on_delete=models.CASCADE, related_name="TypeOfPublication")
    # contentente = RichTextUploadingField("Informações sobre o Edital")
    area = models.ManyToManyField(Area)    
    subArea = models.ManyToManyField(PreferenceArea)
    publicationBy = models.ForeignKey("Users.User", on_delete=models.CASCADE, related_name="PublicationBy")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    editedBy = models.ForeignKey("Users.User", on_delete=models.CASCADE, related_name="EditedBy")
    editDate = models.DateTimeField("Edit Date", auto_now_add=False, null=True, blank=True)    
    is_active = models.BooleanField("Type is active", default=1)
    disabledBy = models.ForeignKey("Users.User", related_name="PublicationDisabledByUser", on_delete=models.CASCADE, null=True, blank=True)
    deactivationTime = models.DateTimeField("Deactivation Time", auto_now_add=False, null=True, blank=True)    
    like = models.IntegerField("Like", default="0", null=True, blank=True)
    deslike = models.IntegerField("Deslike", default=0, null=True, blank=True)
    denounce = models.IntegerField("Denounce", default=0, null=True, blank=True)

    class Meta:
        verbose_name: "Publication"
        verbose_name_plural =  "Publications"
        ordering =  ["title"]
        app_label =  "Administration"

    def __str__(self):
        return str(self.title)

class LikePublication(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="LikePublication")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Like Publication"
        verbose_name_plural = "Like Publications"
        ordering = ['publication']

    def __str__(self):
        return str(self.title)

class DeslikePublication(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="DeslikePublication")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Deslike Publication"
        verbose_name_plural = "Deslike Publications"
        ordering = ['publication']

    def __str__(self):
        return str(self.title)

class DenouncePublication(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="DenouncePublication")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    # falta acrescentar a justificativa
    
    class Meta:
        verbose_name = "Denoouce Publication"
        verbose_name_plural = "Denounce Publications"
        ordering = ['publication']

    def __str__(self):
        return str(self.title)








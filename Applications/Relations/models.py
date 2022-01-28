from django.db import models

from Administration.models import Publication, Article


class LikePublication(models.Model):
    publication = models.ManyToManyField(Publication)
    user = models.ForeignKey("Users.User", on_delete=models.PROTECT, related_name="UserLike")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Like Publication"
        verbose_name_plural = "Like Publications"

    def __str__(self):
        return str(self.user)

class DeslikePublication(models.Model):
    publication = models.ManyToManyField(Publication)
    user = models.ForeignKey("Users.User", on_delete=models.PROTECT, related_name="UserDesLike")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Deslike Publication"
        verbose_name_plural = "Deslike Publications"

    def __str__(self):
        return str(self.user)

class LikeArticle(models.Model):
    publication = models.ManyToManyField(Article)
    user = models.ForeignKey("Users.User", on_delete=models.PROTECT, related_name="UserLikeArticle")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Like Notice"
        verbose_name_plural = "Like Notices"

    def __str__(self):
        return str(self.user)

class DeslikeNotice(models.Model):
    publication = models.ManyToManyField(Article)
    user = models.ForeignKey("Users.User", on_delete=models.PROTECT, related_name="UserDesLikeArticle")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)

    class Meta:
        verbose_name = "Deslike Notice"
        verbose_name_plural = "Deslike Notice"

    def __str__(self):
        return str(self.user)


class DenouncePublication(models.Model):
    publication = models.ForeignKey("Administration.Publication", on_delete=models.CASCADE, related_name="DenouncePublication")
    justification = models.ForeignKey("Administration.Denounce", on_delete=models.PROTECT, related_name="JustificationOfTheDenounce")
    user = models.ForeignKey("Users.User", on_delete=models.PROTECT, related_name="UserDenounce")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    
    class Meta:
        verbose_name = "Denoouce Notice"
        verbose_name_plural = "Denounce Notice"
        ordering = ['publication']

    def __str__(self):
        return str(self.title)

class DenounceArticle(models.Model):
    publication = models.ForeignKey("Administration.Article", on_delete=models.CASCADE, related_name="DenounceOfTheNotice")
    justification = models.ForeignKey("Administration.Denounce", on_delete=models.PROTECT, related_name="JustificationOfTheDenounceNotice")
    user = models.ForeignKey("Users.User", on_delete=models.PROTECT, related_name="UserDenounceNotice")
    creationTime = models.DateTimeField("Creation Time", auto_now_add=True)
    
    class Meta:
        verbose_name = "Denoouce Article"
        verbose_name_plural = "Denounce Articles"
        ordering = ['publication']

    def __str__(self):
        return str(self.title)
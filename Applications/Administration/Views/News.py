from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status




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
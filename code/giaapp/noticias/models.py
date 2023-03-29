from django.db import models

# Create your models here.
class Publicacion(models.Model):

    class TipoPublicacion(models.TextChoices):
        NOTICIA = 'N', 'Noticia'
        EVENTO = 'E', 'Evento'

    titulo = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=1000)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_realizacion = models.DateField() 
    fecha_finalizacion = models.DateField() 
    orden = models.IntegerField()
    imagen = models.CharField(max_length=500)
    pagina_detalles = models.CharField(max_length=500)

    tipoEvento = models.CharField(
        max_length=1,
        choices=TipoPublicacion.choices,
        default=TipoPublicacion.NOTICIA,
    )

    class Meta:
        ordering = ['orden']
        default_permissions = ('add', 'change', 'delete', 'view')
from django.db import models

# Create your models here.
class Course(models.Model):
    #nivel prog = nivel usuario
    name = models.CharField(
        verbose_name='Nome', 
        max_length=100
        )

    slug = models.SlugField(
        verbose_name='Atalho'
        )

    description = models.TextField(
        verbose_name='Descrição', 
        blank=True,
        )
    #blank=true é campo não obrigatório

    start_date = models.DateField(
        verbose_name='Data de inicio', 
        blank=True,
        null=True       
        )
    
    #imagem (django nao armazena imagens no db e sim seu path para um caminho fisico)
    #imagem que o usuario vai fazer upload
    #vai contatenar a partir do MEDIA_ROOT
    image = models.ImageField(
        upload_to='courses/images', 
        verbose_name='Imagem',
        null=True,
        blank=True
        )

    created_at = models.DateTimeField(
        'Criado em', 
        auto_now_add=True
        )
    #auto_now_add = cria automaticamente a data e hora atual

    updated_at = models.DateTimeField(
        'Atualizado em', 
        auto_now=True
        )
    #auto_now = pega automaticamente a data da hora atual e atualiza por cima da já criada


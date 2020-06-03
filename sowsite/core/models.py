from django.db import models

from stdimage.models import StdImageField


class Equipe (models.Model) :
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    imagem = StdImageField('Imagem', upload_to='Equipe')
    linkedin = models.CharField('Linkedin', max_length=100, default='#')
    

    class Meta : 
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self) :
        return self.nome


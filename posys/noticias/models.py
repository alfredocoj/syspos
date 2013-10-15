# Arquivo de modelo 
from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Artigo(models.Model):
	id = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=100L)
	conteudo = models.TextField()
	publicacao = models.DateTimeField(default=datetime.now, blank=True)
	class Meta:
		db_table = 'artigos'
		ordering = ['-publicacao']
	def __unicode__(self):
		return u'%s' % (self.titulo)
	def get_absolute_url(self):
		return '/noticias/artigos/%d/editar'%self.id

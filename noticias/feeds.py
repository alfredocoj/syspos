from django.contrib.syndication.views import Feed

from noticias.models import Artigo

class UltimosArtigos(Feed):
	title = 'Ultimas Noticias do Curso'
	link = '/'

	def items(self):
		return Artigo.objects.all()

	def item_link(self, artigo):
		return '/artigos/%d/'%artigo.id
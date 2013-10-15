from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext

from models import Artigo

def home(request):
    return render_to_response('noticias/index.html', locals(), context_instance=RequestContext(request))


def ver_artigos(request, artigos_id):
	try:
		artigo = Artigo.objects.get(id=artigos_id)
	except Artigo.DoesNotExist:
		raise Http404
	return render_to_response('noticias/v-artigos.html', locals(), context_instance=RequestContext(request))

def listar_artigos(request):
	artigos = Artigo.objects.all()
	return render_to_response('noticias/l-artigos.html', locals(), context_instance=RequestContext(request))

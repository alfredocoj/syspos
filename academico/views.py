from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from academico.models import Alunos
from academico.models import Professores
from academico.models import Cursos
from academico.models import Areas
from academico.models import Disciplinas
from academico.models import Curriculos
from academico.models import Cidades
from academico.models import Turmas
from academico.models import PeriodosLetivos

def home(request):
    return render_to_response('academico/index.html', locals(), context_instance=RequestContext(request))

def entrar(request):
    titulo = 'Login'
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('academico/index.html', locals(), context_instance=RequestContext(request))
        else:
            return render_to_response('academico/login.html', locals(), context_instance=RequestContext(request))
    else:
        return render_to_response('academico/login.html', locals(), context_instance=RequestContext(request))

def sair(request):
    titulo = 'Login'
    logout(request)
    return render_to_response('academico/login.html', locals(), context_instance=RequestContext(request))

@login_required(login_url='/academico/entrar/')
def ver_alunos(request,  alunos_id):
    try:
        aluno = Alunos.objects.get(id=alunos_id)
    except Alunos.DoesNotExist:
        raise Http404
    return render_to_response('academico/v-alunos.html', locals(), context_instance=RequestContext(request))


@login_required(login_url='/academico/entrar/')
def listar_alunos(request, classe_form, alunos_id=None):
    titulo = 'Cadastro de Alunos'
    ver_form = 0
    alunos = Alunos.objects.all()
    if alunos_id:
        aluno = get_object_or_404(classe_form._meta.model, id=alunos_id)
        ver_form = 1
    else:
        aluno = None
    if request.method == 'POST':
        form = classe_form(request.POST, instance=aluno)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.save()
            return HttpResponseRedirect(aluno.get_absolute_url())
    else:
        form = classe_form(instance=aluno)
    return render_to_response('academico/l-alunos.html',  locals(),  context_instance=RequestContext(request))

def ver_professores(request,  professores_id):
    try:
        professor = Professores.objects.get(id=professores_id)
    except Professores.DoesNotExist:
        raise Http404
    return render_to_response('academico/v-professores.html', locals(), context_instance=RequestContext(request))

def listar_professores(request, classe_form, professores_id=None):
    titulo = 'Cadastro de Professores'
    ver_form = 0
    professores = Professores.objects.all()
    if professores_id:
        professor = get_object_or_404(classe_form._meta.model, id=professores_id)
        ver_form = 1
    else:
        professor = None
    if request.method == 'POST':
        form = classe_form(request.POST, instance=professor)
        if form.is_valid():
            professor = form.save(commit=False)
            professor.save()
            return HttpResponseRedirect(professor.get_absolute_url())
    else:
        form = classe_form(instance=professor)
    return render_to_response('academico/l-professores.html',  locals(),  context_instance=RequestContext(request))

def ver_cursos(request,  cursos_id):
    try:
        curso = Cursos.objects.get(id=cursos_id)
    except Cursos.DoesNotExist:
        raise Http404
    return render_to_response('academico/v-cursos.html', locals(), context_instance=RequestContext(request))

def listar_cursos(request, classe_form, cursos_id=None):
    titulo = 'Cadastro de Cursos'
    ver_form = 0
    cursos = Cursos.objects.all()
    if cursos_id:
        curso = get_object_or_404(classe_form._meta.model, id=cursos_id)
        ver_form = 1
    else:
        curso = None
    if request.method == 'POST':
        form = classe_form(request.POST, instance=curso)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            return HttpResponseRedirect(curso.get_absolute_url())
    else:
        form = classe_form(instance=curso)
    return render_to_response('academico/l-cursos.html',  locals(),  context_instance=RequestContext(request))

def excluir_cursos(request, classe_form, cursos_id):
    titulo = 'Cadastro de Cursos'
    ver_form = 0
    cursos = Cursos.objects.get(id=cursos_id)
    cursos.delete()
    
    return render_to_response('academico/l-cursos.html',  locals(),  context_instance=RequestContext(request))

    #return render_to_response('academico/l-cursos.html',  locals(),  context_instance=RequestContext(request))


def listar_areas(request, classe_form, cursos_id, areas_id=None):
    titulo = 'Cadastro de Areas'
    ver_form = 0
    curso = Cursos.objects.get(id=cursos_id)
    areas = Areas.objects.filter(cursos_id=cursos_id)
    if areas_id:
        area = get_object_or_404(classe_form._meta.model, id=areas_id)
        ver_form = 1
    else:
        area = None
    if request.method == 'POST':
        form = classe_form(request.POST, instance=area)
        if form.is_valid():
            area = form.save(commit=False)
            area.save()
            return HttpResponseRedirect(area.get_absolute_url())
    else:
        form = classe_form(instance=area)
    return render_to_response('academico/l-areas.html',  locals(),  context_instance=RequestContext(request))

def listar_disciplinas(request, classe_form, cursos_id, disciplinas_id=None):
    titulo = 'Cadastro de Disciplinas'
    ver_form = 0
    curso = Cursos.objects.get(id=cursos_id)
    disciplinas = Disciplinas.objects.filter(cursos_id=cursos_id)
    if disciplinas_id:
        disciplina = get_object_or_404(classe_form._meta.model, id=disciplinas_id)
        ver_form = 1
    else:
        disciplina = None
    if request.method == 'POST':
        form = classe_form(request.POST, instance=disciplina)
        if form.is_valid():
            disciplina = form.save(commit=False)
            disciplina.save()
            return HttpResponseRedirect(disciplina.get_absolute_url())
    else:
        form = classe_form(instance=disciplina)
    return render_to_response('academico/l-disciplinas.html',  locals(),  context_instance=RequestContext(request))

def listar_curriculos(request, classe_form, cursos_id, curriculos_id=None):
    titulo = 'Cadastro de Curriculos'
    ver_form = 0
    curso = Cursos.objects.get(id=cursos_id)
    curriculos = Curriculos.objects.filter(cursos_id=cursos_id)
    if curriculos_id:
        curriculo = get_object_or_404(classe_form._meta.model, id=curriculos_id)
        ver_form = 1
    else:
        curriculo = None
    if request.method == 'POST':
        form = classe_form(request.POST, instance=curriculo)
        if form.is_valid():
            curriculo = form.save(commit=False)
            curriculo.save()
            return HttpResponseRedirect(curriculo.get_absolute_url())
    else:
        form = classe_form(instance=curriculo)
    return render_to_response('academico/l-curriculos.html',  locals(),  context_instance=RequestContext(request))

    #def ver_turmas(request,  turmas_id):
    #try:
    #    turmas = Turmas.objects.get(id=turmas_id)
    #except Turmas.DoesNotExist:
    #    raise Http404
    #return render_to_response('academico/v-turmas.html', locals(), context_instance=RequestContext(request)


def listar_turmas(request, classe_form, cursos_id, turmas_id=None):
    titulo = 'Cadastro de Turmas'
    ver_form = 0
    curso = Cursos.objects.get(id=cursos_id)
    turmas = Turmas.objects.filter(cursos_id=cursos_id)
    if turmas_id:
        turma = get_object_or_404(classe_form._meta.model, id=turmas_id)
        ver_form = 1
    else:
        turma = None
    if request.method == 'POST':
        form = classe_form(request.POST, instance=turma)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.save()
            return HttpResponseRedirect(turma.get_absolute_url())
    else:
        form = classe_form(instance=turma)
    return render_to_response('academico/l-turmas.html',  locals(),  context_instance=RequestContext(request))


def listar_periodos(request, classe_form, cursos_id, periodos_id=None):
    titulo = 'Cadastro de Periodos Letivos'
    ver_form = 0
    curso = Cursos.objects.get(id=cursos_id)
    periodos = PeriodosLetivos.objects.filter(cursos_id=cursos_id)
    if periodos_id:
        periodo = get_object_or_404(classe_form._meta.model, id=periodos_id)
        ver_form = 1
    else:
        periodo = None
    if request.method == 'POST':
        form = classe_form(request.POST, instance=periodo)
        if form.is_valid():
            periodo = form.save(commit=False)
            periodo.save()
            return HttpResponseRedirect(periodo.get_absolute_url())
    else:
        form = classe_form(instance=periodo)
    return render_to_response('academico/l-periodos.html',  locals(),  context_instance=RequestContext(request))


def excluir_periodos(request, classe_form, cursos_id, periodos_id=None):
    #titulo = 'Cadastro de Periodos Letivos'
    #ver_form = 0
    cursos = Cursos.objects.get(id=cursos_id)
    #periodos = PeriodosLetivos.objects.get(id=periodos_id)
    periodos = PeriodosLetivos.objects.filter(cursos_id=cursos_id).delete()
    #p = cursos.objects.filter()
    #p.delete()
    #periodos = PeriodosLetivos.objects.get(id=periodos_id)
    #periodos.delete()
    
    return render_to_response('academico/l-periodos.html',  locals(),  context_instance=RequestContext(request))
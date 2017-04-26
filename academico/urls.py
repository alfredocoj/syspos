from django.conf.urls import patterns, url, include

from academico import views

from forms import FormAlunos
from forms import FormProfessores
from forms import FormCursos
from forms import FormAreas
from forms import FormDisciplinas
from forms import FormCurriculos
from forms import FormTurmas
from forms import FormPeriodosLetivos

urlpatterns = patterns('',
                       url(r'^$', 'academico.views.home', name='home'),
                       url(r'^entrar/$', 'academico.views.entrar'),
                       url(r'^sair/$', 'academico.views.sair'),
                       # Alunos
    url(r'^alunos/novo/$', 'academico.views.listar_alunos', {'classe_form': FormAlunos}),
                       url(r'^alunos/(?P<alunos_id>\d+)/editar/$', 'academico.views.listar_alunos', {'classe_form': FormAlunos}),
                       url(r'^alunos/(?P<alunos_id>\d+)/$', 'academico.views.ver_alunos'),
                       url(r'^alunos/', 'academico.views.listar_alunos', {'classe_form': FormAlunos}),
                       # Professores
    url(r'^professores/novo/$', 'academico.views.listar_professores', {'classe_form': FormProfessores}),
                       url(r'^professores/(?P<professores_id>\d+)/editar/$', 'academico.views.listar_professores', {'classe_form': FormProfessores}),
                       url(r'^professores/(?P<professores_id>\d+)/$', 'academico.views.ver_professores'),
                       url(r'^professores/', 'academico.views.listar_professores', {'classe_form': FormProfessores}),
                       # Cursos
    url(r'^cursos/novo/$', 'academico.views.listar_cursos', {'classe_form': FormCursos}),
                       url(r'^cursos/(?P<cursos_id>\d+)/editar/$', 'academico.views.listar_cursos', {'classe_form': FormCursos}),
                       url(r'^cursos/(?P<cursos_id>\d+)/excluir/$', 'academico.views.excluir_cursos', {'classe_form': FormCursos}),
                       url(r'^cursos/(?P<cursos_id>\d+)/$', 'academico.views.ver_cursos'),
                       url(r'^cursos/$', 'academico.views.listar_cursos', {'classe_form': FormCursos}),
                       # Detalhes do Curso
    # -- Areas
    url(r'^cursos/(?P<cursos_id>\d+)/areas/(?P<areas_id>\d+)/editar/$', 'academico.views.listar_areas', {'classe_form': FormAreas}),
                       url(r'^cursos/(?P<cursos_id>\d+)/areas/$', 'academico.views.listar_areas', {'classe_form': FormAreas}),
                       # -- Disciplinas
    url(r'^cursos/(?P<cursos_id>\d+)/disciplinas/(?P<disciplinas_id>\d+)/editar/$',
        'academico.views.listar_disciplinas', {'classe_form': FormDisciplinas}),
                       url(r'^cursos/(?P<cursos_id>\d+)/disciplinas/$', 'academico.views.listar_disciplinas', {'classe_form': FormDisciplinas}),
                       # -- Curriculos
    url(r'^cursos/(?P<cursos_id>\d+)/curriculos/(?P<curriculos_id>\d+)/editar/$', 'academico.views.listar_curriculos', {'classe_form': FormCurriculos}),
                       url(r'^cursos/(?P<cursos_id>\d+)/curriculos/$', 'academico.views.listar_curriculos', {'classe_form': FormCurriculos}),
                       # -- Turmas
    url(r'^cursos/(?P<cursos_id>\d+)/turmas/(?P<turmas_id>\d+)/editar/$', 'academico.views.listar_turmas', {'classe_form': FormTurmas}),
                       url(r'^cursos/(?P<cursos_id>\d+)/turmas/$', 'academico.views.listar_turmas', {'classe_form': FormTurmas}),
                       # -- Periodos Letivos
    url(r'^cursos/(?P<cursos_id>\d+)/periodos/(?P<periodos_id>\d+)/editar/$', 'academico.views.listar_periodos', {'classe_form': FormPeriodosLetivos}),
                       url(r'^cursos/(?P<cursos_id>\d+)/periodos/(?P<periodos_id>\d+)/excluir/$',
                           'academico.views.excluir_periodos', {'classe_form': FormPeriodosLetivos}),
                       url(r'^cursos/(?P<cursos_id>\d+)/periodos/$', 'academico.views.listar_periodos', {'classe_form': FormPeriodosLetivos}),

                       )

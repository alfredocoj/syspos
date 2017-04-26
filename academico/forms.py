from django import forms
from django.db import models
from django.forms.extras.widgets import SelectDateWidget

from models import Alunos
from models import Professores
from models import Cursos


from models import Areas
from models import Disciplinas
from models import Curriculos
from models import PeriodosLetivos
from models import Turmas

def make_custom_datefield(f):
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%d/%m/%Y'
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield

class FormAlunos(forms.ModelForm):
	formfield_callback = make_custom_datefield
	class Meta:
		model = Alunos
	def __init__(self, *args, **kwargs):
		super(FormAlunos, self).__init__(*args, **kwargs)
		self.fields['dt_nascimento'].label = "Data de Nascimento"
		self.fields['cpf'].label = "CPF"
		self.fields['rg'].label = "RG"
		self.fields['dt_emissao_rg'].label = "Data de Emissao"
		self.fields['uf_emissao_rg'].label = "UF RG"
		self.fields['telefone1'].label = "Telefone 1"
		self.fields['telefone2'].label = "Telefone 2"
		self.fields['telefone3'].label = "Telefone 3"
		self.fields['telefone4'].label = "Telefone 4"
		self.fields['email1'].label = "E-Mail 1"
		self.fields['email2'].label = "E-Mail 2"

class FormProfessores(forms.ModelForm):
	formfield_callback = make_custom_datefield
	class Meta:
		model = Professores
	def __init__(self, *args, **kwargs):
		super(FormProfessores, self).__init__(*args, **kwargs)
		self.fields['dt_nascimento'].label = "Data de Nascimento"
		self.fields['cpf'].label = "CPF"
		self.fields['rg'].label = "RG"
		self.fields['dt_emissao_rg'].label = "Data de Emissao"
		self.fields['uf_emissao_rg'].label = "UF RG"
		self.fields['telefone1'].label = "Telefone 1"
		self.fields['telefone2'].label = "Telefone 2"
		self.fields['telefone3'].label = "Telefone 3"
		self.fields['telefone4'].label = "Telefone 4"
		self.fields['email1'].label = "E-Mail 1"
		self.fields['email2'].label = "E-Mail 2"

class FormCursos(forms.ModelForm):
	formfield_callback = make_custom_datefield
	class Meta:
		model = Cursos
	def __init__(self, *args, **kwargs):
		super(FormCursos, self).__init__(*args, **kwargs)
		self.fields['ch'].label = "Carga Horaria"
		self.fields['dt_inicio'].label = "Data de Inicio"
		self.fields['dt_fim'].label = "Data de Termino"

class FormAreas(forms.ModelForm):
	class Meta:
		model = Areas
	def __init__(self, *args, **kwargs):
		super(FormAreas, self).__init__(*args, **kwargs)

class FormDisciplinas(forms.ModelForm):
	class Meta:
		model = Disciplinas
	def __init__(self, *args, **kwargs):
		super(FormDisciplinas, self).__init__(*args, **kwargs)
		self.fields['ch'].label = "Carga Horaria"

class FormCurriculos(forms.ModelForm):
	class Meta:
		model = Curriculos
	def __init__(self, *args, **kwargs):
		super(FormCurriculos, self).__init__(*args, **kwargs)

class  FormTurmas(forms.ModelForm):
	class Meta:
		model = Turmas
	def __init__(self, *args, **kwargs):
		super( FormTurmas, self).__init__(*args, **kwargs)
		
class FormPeriodosLetivos(forms.ModelForm):
	formfield_callback = make_custom_datefield
	class Meta:
		model = PeriodosLetivos
	def __init__(self, *args, **kwargs):
		super( FormPeriodosLetivos, self).__init__(*args, **kwargs)
		self.fields['dt_inicio'].label = "Data de Inicio"
		self.fields['dt_fim'].label = "Data de Termino"
		self.fields['prazos_entregas'].label = "Prazo de Entrega"
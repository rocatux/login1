
from django import forms
from .models import ClienteModel
from .models import IngresarProductoModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioForm(forms.ModelForm):
	class Meta:
		model=ClienteModel
		fields='__all__'

class RegistroForm(UserCreationForm):
	class Meta:
		model=User
		fields=[
		'username',
		'first_name',
		'last_name',
		'email',
		'password1',
		'password2',

		]
		labels= {
		'username': 'Nombre de usuario',
		'first_name': 'Nombre',
	        'last_name': 'Apellidos',
	        'email': 'Correo',
	        'password1': 'contraseña',
	        'password2': 'contraseña2',


		}

class IngresarProductoForm(forms.ModelForm):
	class Meta:
		model = IngresarProductoModel
		fields = '__all__'

		








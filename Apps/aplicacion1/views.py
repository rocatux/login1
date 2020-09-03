from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView
from django.shortcuts import redirect
from .models import ClienteModel
from .forms import UsuarioForm
from .forms import IngresarProductoForm
from .models import IngresarProductoModel
from Apps.aplicacion1.forms import RegistroForm

# Create your views here.

class Informacion1View(TemplateView):
	template_name='index.html'

class Informacion2View(TemplateView):
	template_name='informacion.html'

class UsuarioView(CreateView):
	model = User
	template_name='usuario.html'
	form_class= RegistroForm
	success_url = reverse_lazy('app1:inicio')

class IngresarProductoView(CreateView):
	template_name = 'ingresarproducto.html'
	form_class = IngresarProductoForm
	success_url = reverse_lazy('app1:inicio')

class ListaProductosView(ListView):
	template_name = 'listaproductos.html'
	model = IngresarProductoModel

	def get_queryset(self):
		return IngresarProductoModel.objects.all()



		


#def producto_editar (request id):
#		IngresarProductoModel = IngresarProductoModel.objects.get(id=id)
#		if request.method=='GET':
#			form = IngresarProductoForm(instance=IngresarProductoModel)
#		else:
#			form = IngresarProductoForm(request.POST, instance = IngresarProductoModel)
#			if form.is_valid():
#				form.save()
#				return redirect('IngresarProductoModel:listaProducto')
#				return render(request, 'IngresarProductoModel/listarproductos.html', {'form':form}) 


	

#class LoginView(FormView):
	#template_name='login.html'
	#form_class = AuthenticationForm
	#success_url = reverse_lazy('app1:inicio')

	#def form_valid (self, form):
		#login(self.request, form.get_user())
		#return super (LoginView, self) .form_valid (form)


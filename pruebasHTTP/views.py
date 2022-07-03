from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Usuario
from .forms import UsuarioForm

class Login(TemplateView):
    template_name = "pruebasHttp/index.html"

class Usuarios(ListView):
    template_name = 'usuarios/home.html'
    model = Usuario
    context_object_name = 'listado'


def get_usuario(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UsuarioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UsuarioForm()

    return render(request, 'formulario/registro.html', {'form': form})
    



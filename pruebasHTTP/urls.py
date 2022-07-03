from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('listado', views.Usuarios.as_view(), name='listado'), 
    path('registro', views.get_usuario, name='registro')
]

urlpatterns = format_suffix_patterns(urlpatterns)


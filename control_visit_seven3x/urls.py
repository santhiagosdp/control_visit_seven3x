
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('contatos/', views.contatos, name='contatos'),
    path('accounts/', include('django.contrib.auth.urls'))

    
]
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
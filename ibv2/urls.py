from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
    path('classificados', views.classificados, name='classificados'),
    path('contato',views.contato, name='contato'),
    path('destaque/<int:id>',views.destaque, name='destaque'),
    path('eventos',views.eventos,name='eventos'),
    path('programacao',views.programacao, name='programacao'),
    path('publicacao/<int:id>',views.publicacao, name='publicacao'),
    path('sobre',views.sobre,name='sobre'),
    path("ckeditor/", include('ckeditor_uploader.urls')),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

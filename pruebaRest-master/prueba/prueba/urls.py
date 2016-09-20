from django.conf.urls import include, url
from django.contrib import admin
from academico.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'materia', MateriaViewSet)
router.register(r'alumno', AlumnoViewSet)
router.register(r'nota', NotaViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

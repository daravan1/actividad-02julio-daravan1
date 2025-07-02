
from django.urls import path
# se importa las vistas de la aplicación
from administrativo import views

urlpatterns = [
        path('', views.index, name='index'),
        path('detalle/matricula/<int:id>', views.detalle_matricula,
            name='detalle_matricula'),
        path('crear/nueva/matricula', views.crear_matricula,
            name='crear_matricula'),
        path('editar/matricula/<int:id>', views.editar_matricula,
                name='editar_matricula'),
        path('detalle/estudiante/<int:id>', views.detalle_estudiante,
            name='detalle_estudiante'),
        path('crear/nuevo/estudiante', views.crear_estudiante,
            name='crear_estudiante'),
        path('crear/nuevo/modulo', views.crear_modulo,
            name='crear_modulo'),
        path('ver/modulos', views.ver_modulos,
            name='ver_modulos'),
 ]

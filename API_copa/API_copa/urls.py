from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_copa import views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from app_copa.views import GrupoViewSet, TecnicoViewSet, SelecaoViewSet, JogadorViewSet, JogoViewSet, EventoJogoViewSet



schema_view = get_schema_view(
    openapi.Info(
        title='copa API',
        default_version='v1',
        description='API RESTful para copa do mundo',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
 )


router = DefaultRouter()
router.register(r'grupos', GrupoViewSet, basename='grupo')
router.register(r'tecnicos', TecnicoViewSet, basename='tecnico')
router.register(r'selecoes', SelecaoViewSet, basename='selecao')
router.register(r'jogadores', JogadorViewSet, basename='jogador')
router.register(r'jogos', JogoViewSet, basename='jogo')
router.register(r'eventos', EventoJogoViewSet, basename='evento')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),


]



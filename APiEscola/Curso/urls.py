from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    CursoAPIView,
    CursosAPIView,
    AvaliacaoAPIView,
    AvaliacoesAPIView,
    CursoViewSet,
    AvaliacaoViewSet)


router = SimpleRouter()
router.register('Cursos', CursoViewSet)
router.register('Avaliacoes', AvaliacaoViewSet)


urlpatterns = [
    path('Cursos/', CursosAPIView.as_view(), name='Cursos'),
    path('Cursos/<int:pk>', CursoAPIView.as_view(), name='Curso'),
    path('Cursos/<int:Curso_pk>/Avaliacoes/', AvaliacoesAPIView.as_view(), name='Curso_Avaliacoes'),
    path('Cursos/<int:Curso_pk>/Avaliacoes/<int:Avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='Curso_Avaliacao'),
    path('Avaliacoes/', AvaliacoesAPIView.as_view(), name='Avaliacoes'),
    path('Avaliacoes/<int:Avaliacao_pk>', AvaliacaoAPIView.as_view(), name='Avaliacao'),
]


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializers, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    Curso de API REST 'Cursos'
    """
    def get(self, request):
        print(request.user)
        cursos = Curso.objects.all()
        serializer = CursoSerializers(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    Curso de API REST 'Avaliações'
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

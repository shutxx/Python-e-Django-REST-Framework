from rest_framework import serializers
from django.db.models import Avg

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação deve ser um inteiro de 1 a 5')


class CursoSerializers(serializers.ModelSerializer):
    """ Nested Relationship
    Avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    """
    """ HyperLinked Related Fild
        Avaliacoes = serializers.HyperlinkedRelatedField(
            many=True,
            read_only=True,
            view_name='avaliacao-detail'
        )
    """
    # Primary Key Related Field

    Avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    media_avaliacao = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'Avaliacoes',
            'media_avaliacao'
        )

    def get_media_avaliacao(self, obj):
        media = obj.Avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0
        return round(media * 2 / 2)

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import AdDocument


class AdDocumentSerializer(DocumentSerializer):
    class Meta:
        document = AdDocument
        fields = (
            "id",
            "title",
            "description",
            "price",
            "created_at",
        )

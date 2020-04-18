from django_elasticsearch_dsl import Document, fields, Index, KeywordField
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl_drf.compat import StringField
from elasticsearch_dsl import analyzer
from elasticsearch_dsl.analysis import token_filter

from core.models import Ad, Category

ads_index = Index("ads_index")
ads_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

edge_ngram_completion_filter = token_filter(
    'edge_ngram_completion_filter',
    type="edge_ngram",
    min_gram=1,
    max_gram=20
)

edge_ngram_completion = analyzer(
    "edge_ngram_completion",
    tokenizer="standard",
    filter=["lowercase", edge_ngram_completion_filter]
)


@ads_index.doc_type
class AdDocument(Document):
    id = fields.IntegerField(attr='id')

    title = StringField(
        analyzer=html_strip,
        fields={
            'raw': KeywordField(),
            'suggest': fields.CompletionField(),
            'edge_ngram_completion': StringField(
                analyzer=edge_ngram_completion
            ),
        }
    )

    # description = fields.TextField(
    #     analyzer=html_strip,
    #     fields={
    #         'description': fields.TextField(analyzer='keyword'),
    #     }
    # )

    # category = fields.ObjectField(
    #     properties={
    #         'title': fields.TextField(),
    #     }
    # )

    class Django:
        model = Ad  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'price',
            'created_at',
        ]

        related_models = [Category]

    def get_queryset(self):
        return super().get_queryset().select_related('category')

    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Category):
            return related_instance.ad_set.all()

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000

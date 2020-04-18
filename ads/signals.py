from django.db.models.signals import post_save
from django.dispatch import receiver

# Signal to save each new ad instance into ElasticSearch
from core.models import Ad


@receiver(post_save, sender=Ad)
def index_post(sender, instance, **kwargs):
    print(instance)
    instance.indexing()

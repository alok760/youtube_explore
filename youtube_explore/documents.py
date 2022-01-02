from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Video

@registry.register_document
class VideoDocument(Document):
    class Index:
        name = 'video'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Video
         fields = [
             'title',
             'description',
         ]
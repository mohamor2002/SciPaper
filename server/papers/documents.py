from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import paper


@registry.register_document
class paperDocument(Document):
    authors = fields.ListField(fields.TextField())
    def prepare_authors(self ,instance):
        a = []
        for i in instance.auteurs:
            a.append(i)
        return a
    references = fields.ListField(fields.TextField())
    def prepare_references(self ,instance):
        a = []
        for i in instance.references:
            a.append(i)
        return a

    
    keywords = fields.ListField(fields.TextField())
    def prepare_keywords(self, instance):
        a = []
        for i in instance.mots_cles:
            a.append(i)
        return a
    
    
    institutions = fields.ListField(fields.TextField())
    def prepare_institutions(self, instance):
        a = []
        for i in instance.institutions:
            a.append(i)
        return a
    abstract = fields.TextField()
    def prepare_abstract(self, instance):
        return instance.resume
    
    title = fields.TextField()
    def prepare_title(self, instance):
        return instance.titre
    
    id = fields.TextField()
    def prepare_id(self, instance):
        return instance.p_id
    
    date = fields.DateField()
    def prepare_date(self,instance):
        return instance.date_insertion
    class Index:
        # Name of the Elasticsearch index
        name = 'papers'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = paper # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
         
        ]
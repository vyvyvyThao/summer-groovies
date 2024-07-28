from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Class

@register(Class)
class ClassIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = [
        'title',
        'start_date',
        'schedule',
        'body',
        'user',
        'public',
        'path',
        'endpoint',
    ]

    settings = {
        'searchableAttributes': ['title'],
        'attributesForFaceting': ['user', 'public']
    }

    tags = 'get_tags_list'
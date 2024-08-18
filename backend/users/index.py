from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import User

@register(User)
class UserIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = [
        'username',
        'full_name',
        'password',
        'birth_year',
        'facebook_url',
        'phone_number',
        'email',
    ]

    settings = {
        'searchableAttributes': ['username', 'full_name'],
        'attributesForFaceting': ['user']
    }

    # tags = 'get_tags_list'
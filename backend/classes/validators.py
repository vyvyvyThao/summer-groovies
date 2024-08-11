from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Class


def validate_title(value):
        # case insensitive
        qs = Class.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f'{value} is already a class name.')
        return value

def validate_title_no_hello(value):
    if 'hello' in value.lower():
        raise serializers.ValidationError('Hello is not allowed')
    return value

unique_class_title = UniqueValidator(queryset=Class.objects.all(), lookup='iexact')
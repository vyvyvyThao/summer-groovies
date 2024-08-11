from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# from .models import User

def validate_username_no_special_char(value):
    special_chars = ['"', '*', '<', '>', '/', '?', '%', '*', ':', '|']

    for char in special_chars:
        if char in value:
            raise serializers.ValidationError(f'{char} is not allowed in username')
    return value


from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import User
from . import validators

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[validators.validate_username_no_special_char])

    class Meta: 
        model = User
        fields = [
                'username',
                'full_name',
                'password',
                'birth_year',
                'facebook_url',
                'phone_number',
                'email',
            ]
    

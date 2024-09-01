from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import User
from . import validators

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[validators.validate_username_no_special_char])
    class_names = serializers.SerializerMethodField()
    # pk = serializers.IntegerField(source='pk')

    class Meta: 
        model = User
        fields = [
                'pk',
                'username',
                'full_name',
                # 'password',
                'birth_year',
                'facebook_url',
                'phone_number',
                'email',
                'class_names'
            ]
        
    def get_class_names(self, obj):
        return [dance_class.title for dance_class in obj.registered_classes.all()]
    

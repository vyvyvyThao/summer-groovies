from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer, UserClassInlineSerializer
from .models import Class
from . import validators

class ClassSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='class-detail', lookup_field='pk')
    
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_class_title])
    
    class Meta:
        model = Class
        fields = [
            'owner',
            'url',
            'edit_url',
            'title',
            'start_date',
            'end_date',
            'schedule',
            'description',
            'slots_remaining',
        ]
    
    def get_my_user_data(self, obj):
         return {
             'username': obj.user.username
         }

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user

    #     # case insensitive
    #     qs = Class.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already a class name.')
    #     return value
    
    def get_edit_url(self, obj):
        request = self.context.get('request')

        if request is None:
            return None
        # return f'/api/classes/{obj.pk}/'
        return reverse('class-edit', kwargs={'pk': obj.pk}, request=request)
    
    
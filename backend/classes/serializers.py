from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Class

class ClassSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='class-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Class
        fields = [
            'url',
            'edit_url',
            'title',
            'start_date',
            'end_date',
            'email',
            'schedule',
            'description',
            'slots_remaining'
        ]

    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #      print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)
    
    def get_edit_url(self, obj):
        request = self.context.get('request')

        if request is None:
            return None
        # return f'/api/classes/{obj.pk}/'
        return reverse('class-edit', kwargs={'pk': obj.pk}, request=request)
    
    
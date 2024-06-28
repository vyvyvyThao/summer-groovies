from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class UserClassInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='class-detail', 
        lookup_field='pk',
        read_only=True
    )    
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
#     other_classes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User 
        fields = [
            'username',
            'this_does_cause_any_issue',
            'id',
        ]

#     def get_other_classes(self, obj):
#         request = self.context.get('request')
#         print(obj)
#         user = obj
#         my_classes_qs = user.class_set.all()[:4]
#         return UserClassInlineSerializer(my_classes_qs, many=True, context = self.context).data
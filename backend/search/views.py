from rest_framework import generics

from classes.models import Class
from classes.serializers import ClassSerializer

class SearchListView(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q') 
        results = Class.objects.none()

        if q is not None:
            user = None
            
            if self.request.user.is_authenticated:
                user = self.request.user
            
            results = qs.search(q, user=user)
        return results 
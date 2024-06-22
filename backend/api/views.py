import json
# from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from classes.models import Class 
from classes.serializers import ClassSerializer

@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    # instance= Class.objects.all().order_by("?").first()
    # data = {}

    # if instance:
    #     # data = model_to_dict(model_data, fields = ['id', 'title', 'start_date', 'end_date'])
    #     data = ClassSerializer(instance).data
    serializer = ClassSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response({"Invalid": "not good data"}, status=400)
    # return JsonResponse(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})
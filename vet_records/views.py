import json

from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView

from .models import CatRecords

class Cat_Record_Controller(APIView):

    def get(self, request, pk, format=None):
        retval = {}
        cat = CatRecords.objects.get(pk=pk)
        if cat is not None:
            retval['id'] = cat.id
            retval['name'] = cat.name
            retval['birth_date'] = cat.birth_date

        return JsonResponse(retval)

    def post(self, request, format=None):
        name = request.data.get("name")
        birth_date = request.data.get("birth_date")

        CatRecords.objects.create(name=name, birth_date=birth_date)

        return HttpResponse(status=202)

    def put(self, request, pk, format=None):
        cat = CatRecords.objects.get(pk=pk)
        retval = 400
        if cat is not None:
            cat.name = request.data.get("name")
            cat.birth_date = request.data.get("birth_date")
            cat.save()
            retval = 200

        return HttpResponse(status=retval)

    def delete(self, request, pk, format=None):
        CatRecords.objects.filter(pk=pk).delete()
        return HttpResponse(200)
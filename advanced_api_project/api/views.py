from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class ItemList(APIView):
    def get(self, request):
        return Response({"message": "List of items"})

class ItemDetail(APIView):
    def get(self, request, pk):
        return Response({"message": f"Detail of item {pk}"})

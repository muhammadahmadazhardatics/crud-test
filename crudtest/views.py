from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CrudSerializer
from .models import Crud
from django.db.models import Q
class CrudViewSet(viewsets.ViewSet):

    def list(self, request):
        qs = Crud.objects.all()
        serializer = CrudSerializer(qs, many=True, context={"request": request})
        dicr_response = {"error": False, "message": "All List Data", "data": serializer.data}
        return Response(dicr_response)

    def create(self, request):
        try:
            serializers = CrudSerializer(data=request.data, context={"request": request})
            serializers.is_valid(raise_exception=True)
            serializers.save()
            dict_response = {"error": False, "message": "Data save successfully"}
        except:
            dict_response = {"error": True, "message": "Error saving data"}

        return Response(dict_response)

    def retrieve(self,request, pk=None):
        queryset = Crud.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = CrudSerializer(instance, context={"request": request})
        return Response({"error": False, "message": "Single data fetch", "data": serializer.data })

    def update(self,request, pk= None):
        try:
            qs = Crud.objects.all()
            instance = get_object_or_404(qs, pk=pk)
            serializer = CrudSerializer(instance, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Data update successfully"}
        except:
            dict_response = {"error": True, "message": "Error updating data"}
        return Response(dict_response)


    def destroy(self, request, pk=None):
        """Delete object with given pk"""
        queryset = Crud.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        # instance = get_object_or_404(self.get_queryset(), pk=pk)
        instance.delete()
        return Response({"delete": True})


class SearchWithParams(generics.ListAPIView):
    serializer_class = CrudSerializer

    def get_queryset(self):
        queryset = Crud.objects.all()

        firstName = self.request.query_params.get("firstname")
        if firstName is not None:
            queryset  = queryset.filter(name__icontains=firstName)

        return queryset


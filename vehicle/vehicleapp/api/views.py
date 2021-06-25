from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import VehicleModelSerializers, VehicleSerializers
from ..models import Vehicle, VehicleModel
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


class VehicleModelView(APIView):
    @method_decorator(cache_page(60*5))
    def get(self, request):
        queryset = VehicleModel.objects.all()
        serializer = VehicleModelSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class VehicleModelDetail(APIView):
    def put(self, request, pk):
        query = VehicleModel.objects.get(id=pk)
        serializer = VehicleModelSerializers(instance=query, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        query = VehicleModel.objects.get(id=pk)
        #query.soft_delete()
        query.delete()
        return Response('Deleted')


class VehicleView(APIView):
    @method_decorator(cache_page(60*5))
    def get(self, request):
        query = Vehicle.objects.all()
        serializer = VehicleSerializers(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class VehicleDetail(APIView):
    def delete(self, request, pk):
        query = Vehicle.objects.get(id=pk)
        # query.soft_delete()
        query.delete()
        return Response('Deleted')

    def put(self, request, pk):
        query = Vehicle.objects.get(id=pk)
        serializer = VehicleSerializers(instance=query, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# class testClass(APIView):
#     def get(self, request):
#         return Response({'message': 'GET Request'})

#     def post(self, request):
#         return Response({'message': 'POST Request'})

#     def put(self, request):
#         return Response({'message': 'PUT Request'})

#     def delete(self, request):
#         return Response({'message': 'DELETE Request'})

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Klass, Mehmonxona, Travel
from .serializer import KlassSerializer, MehmonxonaSerializer, TravelSerializer



class KlassAPIView(APIView):
    def get(self, request, pk=None):
        if not pk:
            transport = Klass.objects.all()
            return Response({'transport':KlassSerializer(transport, many=True).data})
        try:
            transport = Klass.objects.get(pk=pk)
            serializer = KlassSerializer(transport)
            return Response(serializer.data)
        except Klass.DoesNotExist:
            return Response({'error': 'Transport not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request:Request):
        serializer = KlassSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transport = serializer.save()
        return Response(KlassSerializer(transport).data)
        
    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method PUT not allowed"})
        try:
            transport = Klass.objects.get(pk=pk)
            serializer = KlassSerializer(instance=transport, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_transport = serializer.save()
            return Response(TravelSerializer(updated_transport).data)
        except:
            return Response({"message":"Bunday transport turi yo'q"})
        

    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method DELETE not allowed"})
        try:
            transport = Klass.objects.get(pk=pk)
            transport.delete()
            return Response({"message":"Success"})
        except:
            return Response({"message":"Bunday transport turi yo'q"})






class MehmonxonaAPIView(APIView):
    def get(self, request, pk=None):
        if not pk:
            mehmonxona = Mehmonxona.objects.all()
            return Response({'mehmonxona':MehmonxonaSerializer(mehmonxona, many=True).data})
        try:
            mexmonxona = Mehmonxona.objects.get(pk=pk)
            serializer = MehmonxonaSerializer(mexmonxona)
            return Response(serializer.data)
        except Mehmonxona.DoesNotExist:
            return Response({'error': 'Klass not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request:Request):
        serializer = MehmonxonaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mexmonxona = serializer.save()
        return Response(TravelSerializer(mexmonxona).data)
        

    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method PUT not allowed"})
        try:
            mexmonxona = Mehmonxona.objects.get(pk=pk)
            serializer = MehmonxonaSerializer(instance=mexmonxona, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_mexmonxona = serializer.save()
            return Response(TravelSerializer(updated_mexmonxona).data)
        except:
            return Response({"message":"Bunday mehmonxona turi yo'q"})
        

    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method DELETE not allowed"})
        try:
            mexmonxona = Mehmonxona.objects.get(pk=pk)
            mexmonxona.delete()
            return Response({"message":"Success"})
        except:
            return Response({"message":"Bunday mrhmonxona turi yo'q"})





class TravelAPIView(APIView):
    def get(self, request: Request, pk = None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                return Response(TravelSerializer(travel).data)
            except:
                return Response({"message":"Bunday travel turi yo'q"})
        travel = Travel.objects.all()
        return Response({'travel':TravelSerializer(travel, many=True).data})
    
    def post(self, request:Request):
        serializer = TravelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        travel = serializer.save()
        return Response(TravelSerializer(travel).data)
    
    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method PUT not allowed"})
        try:
            travel = Travel.objects.get(pk=pk)
            serializer = TravelSerializer(instance=travel, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_travel = serializer.save()
            return Response(TravelSerializer(updated_travel).data)
        except:
            return Response({"message":"Bunday travel turi yo'q"})
    
    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"message":"Method DELETE not allowed"})
        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()
            return Response({"message":"Success"})
        except:
            return Response({"message":"Bunday travel turi yo'q"})
    

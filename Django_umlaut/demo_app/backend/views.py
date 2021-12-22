from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import LineA, LineB
from .serializers import LineASerializer, LineBSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


@api_view(["GET", "POST"])
@csrf_exempt
def line_a(request):
    if request.method == "POST":
        data = request.data
        try:
            line_a = LineA.objects.get(pk = data["shift_model"])
            serializer = LineASerializer(line_a,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
        except Exception as err:
            serializer = LineASerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
        return Response({})
    elif request.method == "GET":
        line_a = LineA.objects.all()
        serializer = LineASerializer(line_a, many=True)
        return Response(serializer.data)
    return Response({"Message": "we are supporting only Get and Post methods"}, status=400)


@api_view(["GET", "POST"])
@csrf_exempt
def line_b(request):
    if request.method == "POST":
        data = request.data
        try:
            line_a = LineB.objects.get(pk = data["shift_model"])
            serializer = LineBSerializer(line_a,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
        except Exception as err:
            serializer = LineBSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
        return Response({})
    elif request.method == "GET":
        line_a = LineB.objects.all()
        serializer = LineBSerializer(line_a, many=True)
        return Response(serializer.data)
    return Response({"Message": "we are supporting only Get and Post methods"}, status=400)
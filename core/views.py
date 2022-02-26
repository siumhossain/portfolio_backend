
from os import stat
import re
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import About, Blog, Project,Image
from core.serializers import AboutSerializer, BlogSerializer, ProjectSerializer,ImageSerializer
from django.db.models import Q

# from django.http import HttpResponse

# Create your views here.
@api_view(['GET'])
def about(request):
    if request.method == 'GET':
        obj = About.objects.all()
        serializers = AboutSerializer(obj,many=True)
        if serializers:
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def projects(request):
    if request.method == 'GET':
        obj = Project.objects.all()
        serializers = ProjectSerializer(obj,many=True)
        if serializers:
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def images(request):
    if request.method == 'GET':
        obj = Image.objects.all()
        serializers = ImageSerializer(obj,many=True)
        if serializers:
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def singleProject(request,id):
    if request.method == 'GET':
        obj = Project.objects.get(id=id)
        if obj:
            serializers = ProjectSerializer(obj)
            if serializers:
                return Response(serializers.data,status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def blogs(request):
    if request.method == 'GET':
        obj = Blog.objects.all()
        serializers = BlogSerializer(obj,many=True)
        if serializers:
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def singleBlog(request,id):
    if request.method == 'GET':
        obj = Blog.objects.get(id=id)
        if obj:
            serializers = BlogSerializer(obj)
            if serializers:
                return Response(serializers.data,status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
def search(request,q):
    if request.method == 'GET':
        obj = About.objects.filter(
            Q(title__icontains = q) | Q(description__icontains = q)
        ).distinct()
        if obj:
            serializers = AboutSerializer(obj,many=True)
            return Response(serializers.data,status=status.HTTP_200_OK)
        else:
            obj2 = Project.objects.filter(
                Q(title__icontains = q) | Q(short_description__icontains = q) |
                Q(description__icontains = q)
            ).distinct()
            if obj2:
                serializers = ProjectSerializer(obj2,many=True)
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            else:
                obj3 = Blog.objects.filter(
                    Q(title__icontains = q) | Q(short_description__icontains = q) |
                    Q(description__icontains = q)
                ).distinct()
                if obj3:
                    serializers = BlogSerializer(obj3,many=True)
                    return Response(serializers.data,status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
   

# comment
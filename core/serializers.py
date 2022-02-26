from urllib import request
from django.db import models
from rest_framework import fields, serializers

from core.models import About, Blog, Image, Project



class ProjectSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField("%d-%m-%Y %I:%M %p")
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, instance):
        if instance.thumbnail:
            return instance.thumbnail.url
            
    class Meta:
        model = Project
        fields = ['id','title','short_description','description','thumbnail','created']

    


    

class AboutSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField("%d-%m-%Y %I:%M %p")
    

    class Meta:
        model = About
        fields = ['id','title','description','created']

class ImageSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField("%d-%m-%Y %I:%M %p")

    class Meta:
        model = Image
        fields = ['id','description','file','created']

class BlogSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField("%d-%m-%Y %I:%M %p")
    class Meta:
        model = Blog
        fields = ['id','title','short_description','description','thumbnail','created']
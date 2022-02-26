from django.db import models
from django.db.models.base import Model
from ckeditor_uploader.fields import RichTextUploadingField




# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=300)
    short_description = RichTextUploadingField(blank=True,null=True)
    description = RichTextUploadingField(blank=True,null=True)
    thumbnail = models.FileField()
    created = models.DateTimeField(null=True,blank=True,auto_now=True)

    class Meta:
        ordering = ['-created',]
    def __str__(self):
        return f'{self.id} | {self. title}'




class Image(models.Model):
    description = RichTextUploadingField(blank=True,null=True)
    file = models.FileField()
    created = models.DateTimeField(null=True,blank=True,auto_now=True)

    class Meta:
        ordering = ['-created',]
    def __str__(self):
        return f'{self.id}'

class Blog(models.Model):
    title = models.CharField(max_length=300)
    short_description = RichTextUploadingField(blank=True,null=True)
    description = RichTextUploadingField(blank=True,null=True)
    thumbnail = models.FileField()
    created = models.DateTimeField(null=True,blank=True,auto_now=True)

    class Meta:
        ordering = ['-created',]
    def __str__(self):
        return f'{self.id} | {self. title}'

class About(models.Model):
    title = models.CharField(max_length=300)
    description = RichTextUploadingField(blank=True,null=True)
    created = models.DateTimeField(null=True,blank=True,auto_now=True)

    class Meta:
        ordering = ['-created',]
    def __str__(self):
        return f'{self.id} | {self. title}'


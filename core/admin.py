from django.contrib import admin


from core.models import About, Blog, Image, Project

# Register your models here.
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(Blog)
admin.site.register(About)




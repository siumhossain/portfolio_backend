from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about),
    path('projects/',views.projects),


    path('projects/<str:id>/',views.singleProject),

    path('images/',views.images),
    
    path('search/<str:q>/',views.search),

    path('blogs/',views.blogs),
    path('blog/<str:id>/',views.singleBlog)
]
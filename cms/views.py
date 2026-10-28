from rest_framework import generics
from .models import Project, PageSEO
from .serializers import (
    ProjectListSerializer, 
    ProjectDetailSerializer, 
    PageSEOSerializer
)

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.filter(is_published=True).order_by('-project_Published_date')
    serializer_class = ProjectListSerializer

class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.filter(is_published=True)
    serializer_class = ProjectDetailSerializer
    lookup_field = 'slug'

class PageSEOAPIView(generics.RetrieveAPIView):
    queryset = PageSEO.objects.all()
    serializer_class = PageSEOSerializer
    lookup_field = 'slug'
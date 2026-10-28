from django.urls import path
from .views import ProjectListAPIView, ProjectDetailAPIView, PageSEOAPIView

app_name = 'cms'

urlpatterns = [
    # API Endpoints for Next.js
    path('api/projects/', ProjectListAPIView.as_view(), name='api_project_list'),
    path('api/projects/<slug:slug>/', ProjectDetailAPIView.as_view(), name='api_project_detail'),
    path('api/seo/<slug:slug>/', PageSEOAPIView.as_view(), name='api_page_seo'),
]
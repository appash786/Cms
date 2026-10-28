from django.contrib import admin
from django.urls import path,include
from django_otp.admin import OTPAdminSite

# Convert the default admin site to require OTP
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cms.urls')),  # <-- This pulls in all your cms/urls.py routes
]
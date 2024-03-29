"""tfg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from tfg.views import signup
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Admin urls
admin.site.site_url = 'http://192.168.1.13:8080/'
admin.site.site_header = 'Django Administration - TFG'

# Swagger url configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Swagger API - TFG",
        default_version='v1.0',
        description="U.u",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('rest_framework.urls',
                          namespace='rest_framework')),

    path('api/v1.0/', include('categories.urls')),
    path('api/v1.0/', include('activities.urls')),
    path('api/v1.0/', include('profiles.urls')),

    path('signup/', view=signup, name="signup"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

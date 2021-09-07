"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import permissions
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="캠핑장 정보 API",
      default_version='v1',
      description="전국 무료 캠핑장 정보",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kseungkoo@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('camp/', include('camp.urls')),
    path('board/', include('board.urls')),
    # path('rest-auth/', include('rest_auth.urls')), # Login, Logout 관련 기능
    # path('rest-auth/signup/', include('dj_rest_auth.registration.urls')), # Login, Logout 관련 기능
    path('accounts/', include('dj_rest_auth.urls')), # Login, Logout 관련 기능
    path('accounts/', include('dj_rest_auth.registration.urls')), # Login, Logout 관련 기능
    # path('rest-auth/', include('allauth.urls')), # Login, Logout 관련 기능
    # path('rest-auth/', include('rest_auth.urls')), # Login, Logout 관련 기능

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # url(r'^accounts/', include('dj_rest_auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
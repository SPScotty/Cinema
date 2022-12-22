"""blog_api URL Configuration

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
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from main.views import GenreListView, MovieViewSet, PosterViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Python 23 API",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)




router = DefaultRouter()
router.register('movies', MovieViewSet)

'''
create ---------> movies/ POST
list -----------> movies/ GET
retrieve -------> movies/id/ GET
update ---------> movies/id/ PUT
partial-update -> movies/id/ PATCH
destroy --------> movies/id/ DELETE
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('v1/api/genres/', GenreListView.as_view()),
    path('v1/api/add-image/', PosterViewSet.as_view()),
    path('v1/api/', include(router.urls)),
    path('', include('account.urls')),
]



urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

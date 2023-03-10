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

from main.views import *

swagger_view = get_schema_view(
    openapi.Info(
        title="Giga chads",
        description="makers bootcamp",
        default_version="v1",
    ),
    public=True
)




router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('genres', GenreViewSet)
router.register('posters', MoviePosterViewSet)
router.register('comments',CommentViewSet)



'''
create ---------> object/ POST
list -----------> object/ GET
retrieve -------> object/id/ GET
update ---------> object/id/ PUT
partial-update -> object/id/ PATCH
destroy --------> object/id/ DELETE
'''



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/likes/', LikeViewSet.as_view()),
    path('v1/api/rating/', RatingViewSet.as_view()),
    path('v1/api/favorites/', favourite),
    path('v1/api/', include(router.urls)),
    path('v1/api/account/', include('account.urls')),
    path('docs/', swagger_view.with_ui('swagger', cache_timeout=0)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



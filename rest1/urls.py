"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from rest_framework import routers

from rest1app import views
from django.urls import path,include
from django.contrib import admin
from rest1app.views import DetailsView
from django.conf.urls import  url
from django.views import generic
from django.conf.urls import handler500, handler404
from django.conf import settings
from django.conf.urls.static import static

from django.http import HttpResponse
from rest1app import views as common_views

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

# handler500 = rest1app.views.handler500


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),


   path('error-500-demo/', common_views.error_500, name='error_500'),
   path('error-404-demo/', common_views.error_404, name='error_404'),
    url(r'^articlelists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

handler_404 = common_views.error_404
handler_500 = common_views.error_500

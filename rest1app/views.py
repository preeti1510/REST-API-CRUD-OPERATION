from rest1app.models import Article
from rest_framework import viewsets
from rest1app.serializers import ArticleSerializer
from  rest_framework  import generics
from django.conf import settings
from django.shortcuts import render
from django.template import RequestContext
# from django.shortcuts import get_object_or_201

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

def error_500(request):
    context={}
    context={"project_name":settings.PROJECT_NAME}

    return render(request,'500.html',context)

def error_404(request):
    context={}
    context={"project_name":settings.PROJECT_NAME}

    return render(request,'404.html',context)

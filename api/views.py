from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from backend.models import *
from api.serializers import *

# Create your views here.

class  CategorieViewSet(viewsets.ModelViewSet):

    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer



class  PlatViewSet(viewsets.ModelViewSet):

    queryset = Plat.objects.all()
    serializer_class = PlatSerializer 
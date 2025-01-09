from rest_framework import serializers
from api.models import *


class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
       


class PlatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plat
        fields = '__all__'










# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import *
 
# Create a model serializer
class ApisSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = ApisModel
        fields = ('title', 'description')

class V1Serializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = V1Model
        fields = ('lastname','firstname','sex','region','yearof','age')
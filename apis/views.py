
# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import *
from .models import *
 
# create a viewset
class ApisViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = ApisModel.objects.all()
     
    # specify serializer to be used
    serializer_class = ApisSerializer

class V1ViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = V1Model.objects.all()
     
    # specify serializer to be used
    serializer_class = V1Serializer
from rest_framework.viewsets import ModelViewSet
from mmdb.models import customer
from mmdb import serializers

class customerViewSet(ModelViewSet):
    queryset = customer.objects.all()
    data_list = serializers.data_list
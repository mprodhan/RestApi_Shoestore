from django.shortcuts import render
from api.serializers import ManufacturerSerializer, ShoeSerializer, ShoeTypeSerializer, ShoeColorSerializer
from api.models import Manufacturer, ShoeType, ShoeColor, Shoe
from rest_framework.viewsets import ModelViewSet

class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = "manufacturer"
    queryset = Manufacturer.objects.all()

class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = "shoe type"
    queryset = ShoeType.objects.all()

class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    basename = "shoe color"
    queryset = Shoe.objects.all()

class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    basename = "shoe"
    queryset = Shoe.objects.all()



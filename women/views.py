from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .Serializers import WomenSerializer
from .models import Women
from .services.permissions import CustomPermissionUpdate,CustomPermissionDelete


class WomenApiList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class WomenApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)

class WomenApiDelete(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (CustomPermissionDelete,)

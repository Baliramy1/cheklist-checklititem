from django.shortcuts import render

from django.http import Http404
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    )
from bali.models import CheckList, CheckListItem
from bali.permissions import IsOwner
from bali.serializers import CheckListSerializer, CheckListItemSerializer


class CheckListsAPIView(ListCreateAPIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset
    
class CheckListAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset

class CheckListItemCreateAPIview(CreateAPIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class CheckListItemAPIview(RetrieveUpdateDestroyAPIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset
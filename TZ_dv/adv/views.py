from django.shortcuts import render
from rest_framework import viewsets, generics, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.


class AdvertisementAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class AdvertisementAPIList(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    pagination_class = AdvertisementAPIListPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'data_create']
    ordering = ['price', 'data_create']

    def get_queryset(self):
        queryset = Advertisement.objects.all()
        fields = self.request.GET.get('fields')
        if fields:
            fields = fields.split(',')
            allowed_fields = set(tuple(self.serializer_class.Meta.fields) + tuple(fields))
            self.serializer_class.Meta.fields = tuple(allowed_fields)
        return queryset

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         self.perform_create(serializer)
    #         headers = self.get_success_headers(serializer.data)
    #         response_data = {'id': serializer.instance.pk, 'status': 'success'}
    #         return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    #
    #     response_data = {'status': 'error', 'errors': serializer.errors}
    #     return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


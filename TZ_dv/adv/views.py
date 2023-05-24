from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.forms.models import model_to_dict


def AdvertisementAPIListCreate(request):
    if request.method == 'GET':
        ordering = request.GET.get('ordering', 'price, data_create')
        ordering_fields = [field.strip() for field in ordering.split(',')]
        Advertisements = Advertisement.objects.all().order_by(*ordering_fields)
        ad_list = []
        for ad in Advertisements:
            ad_data = {
                'title': ad.title,
                'image_paths': ad.photos.first().image_path if ad.photos.first() else None,
                'price': ad.price
            }
            ad_list.append(ad_data)
        paginator = Paginator(ad_list, 20)
        page_number = request.GET.get('page')
        page_advertisements = paginator.get_page(page_number)
        return JsonResponse({'Ответ': list(page_advertisements)})

    if request.method == 'POST':
        data = request.POST.dict()
        new_ad =

def AdvertisementAPI(request, pk):
    if request.method == 'GET' and pk:
        Ad = Advertisement.objects.get(pk=pk)
        image_paths = list(Ad.photos.all().values_list('image_path', flat=True)) if Ad.photos.all().values_list('image_path', flat=True) else None
        ad_data = {
            'title': Ad.title,
            'image_paths': image_paths[0],
            'price': Ad.price
        }
        if request.GET.get('fields', None):
            fields = request.GET['fields'].split(',')
            if 'description' in fields:
                ad_data['description'] = Ad.description
            if 'photos' in fields:
                ad_data['image_paths'] = image_paths

        return JsonResponse({'Ответ': ad_data})

def AdvertisementAPICreate(request):



# class AdvertisementAPIListPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 1000
#
#
# class AdvertisementAPIList(viewsets.ModelViewSet):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     pagination_class = AdvertisementAPIListPagination
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['price', 'data_create']
#     ordering = ['price', 'data_create']
#
#     def get_queryset(self):
#         queryset = Advertisement.objects.all()
#         fields = self.request.GET.get('fields')
#         if fields:
#             fields = fields.split(',')
#             allowed_fields = set(tuple(self.serializer_class.Meta.fields) + tuple(fields))
#             self.serializer_class.Meta.fields = tuple(allowed_fields)
#         return queryset



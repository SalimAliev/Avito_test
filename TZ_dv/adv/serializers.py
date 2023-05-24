from .models import *
from rest_framework import serializers


# class PhotoLinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = ['image_path']
#
#
# class AdvertisementSerializer(serializers.ModelSerializer):
#     photo = PhotoLinkSerializer(many=True, required=False)
#
#     class Meta:
#         model = Advertisement
#         fields = ['title', 'price', 'photo']
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['photo'] = data['photo'][0] if data['photo'] else None
#         return data
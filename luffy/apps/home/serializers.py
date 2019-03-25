from rest_framework.serializers import ModelSerializer
from .models import bannerInfo
class BannerInfoSerializer(ModelSerializer):
    """轮播图序列化器"""
    class Meta:
        model=bannerInfo
        fields = ("image","link","orders")
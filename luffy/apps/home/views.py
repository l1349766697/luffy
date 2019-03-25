from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import bannerInfo
class BannerInfoAPIView(APIView):
    """
    轮播图列表
    """
    def get(self,request):
        # 获取数据
        banners = bannerInfo.objects.filter(Q(is_show=True) & Q(is_delete=False)).order_by("-orders")
        # 调整banners的images字段

        # 序列化
        data = []
        for item in banners:
            data.append({
              # 拼接图片的url地址
              "image": "/static/" + item.image.url,
              "link":item.link,
              "orders":item.orders,
            })
        return Response(data)
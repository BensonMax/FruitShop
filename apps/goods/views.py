from .serializers import GoodsSeriallizer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods

class GoodListView(APIView):
    """
    List all goods
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSeriallizer(goods, many=True)
        return Response(goods_serializer.data)
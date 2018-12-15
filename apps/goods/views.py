from .serializers import GoodsSeriallizer
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from .models import Goods
from rest_framework import viewsets


#分页设置
class GoodsResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class GoodListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    List all goods
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSeriallizer
    pagination_class = GoodsResultsSetPagination


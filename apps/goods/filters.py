
from django_filters import rest_framework as filters
import django_filters
from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤
    """
    #配置过滤行为
    price_min = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    #name = django_filters.CharFilter(field_name="name",lookup_expr='icontains') 模糊查询

    class Meta:
        model = Goods
        fields = ['price_min','price_max','name']


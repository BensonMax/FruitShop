
from django_filters import rest_framework as filters
import django_filters
from .models import Goods
from django.db.models import Q


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤
    """
    # 配置过滤行为
    price_min = filters.NumberFilter(
        field_name="shop_price", lookup_expr='gte')
    price_max = filters.NumberFilter(
        field_name="shop_price", lookup_expr='lte')
    # name =
    # django_filters.CharFilter(field_name="name",lookup_expr='icontains')
    # 模糊查询
    top_category = django_filters.NumberFilter(method="top_category_filter")

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category__id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name', 'is_hot']

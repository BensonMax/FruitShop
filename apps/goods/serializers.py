from rest_framework import serializers

from goods.models import Goods,GoodsCategory,GoodsImage


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many =True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSeriallizer(serializers.ModelSerializer):
    """
    商品列表序列化
    """
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"




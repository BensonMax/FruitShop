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


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image", )

class GoodsSeriallizer(serializers.ModelSerializer):
    """
    商品列表序列化
    """
    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        exclude = ('goods_desc',)



from rest_framework import mixins
from rest_framework import viewsets

from .models import UserFav
from .serializers import UserFavSerializers



class UserFavViewset(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    """
    用户收藏功能
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializers


"""FruitShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
import xadmin
from FruitShop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodListViewSet,CategoryViewSet
from users.views import SmsCodeViewset,UserViewset


router = DefaultRouter()
#配置goods的url
router.register(r'goods', GoodListViewSet,base_name="goods")
#配置categorys的url
router.register(r'categorys', CategoryViewSet,base_name="categorys")
#配置code
router.register(r'codes', SmsCodeViewset,base_name="codes")

#配置users
router.register(r'users', UserViewset,base_name="users")


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),    #账号 admin 密码 admin123
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),   #drf 登陆url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),


    #商品列表页
    url(r'^', include(router.urls)),
    url(r'docs/',include_docs_urls(title="水果超市API")),
    #drf 自带的token
    url(r'^api-token-auth/', views.obtain_auth_token),
    #jwt的认证接口
    url(r'^jwt_auth/', obtain_jwt_token),
]

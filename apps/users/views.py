from django.shortcuts import render

# Create your views here.
from random import choice

from django.contrib.auth import get_user_model
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler

from utils.yunpian import YunPian
from FruitShop.settings import APIKEY
from .models import VerifyCode
from .serializers import SmsSerializer, UserRegSerializer, UserDetailSerializer

User = get_user_model()

class SmsCodeViewset(CreateModelMixin,viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]
        yun_pian = YunPian(APIKEY)

        code = self.generate_code()

        sms_status = yun_pian.send_sms(code=code, mobile=mobile)

        if sms_status["code"] != 0:
            return Response({
                "mobile": sms_status["msg"]
            }, status = status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code,mobile= mobile)
            code_record.save()

            return Response({
                "mobile": sms_status["msg"]
            }, status = status.HTTP_201_CREATED)



class UserViewset(CreateModelMixin, mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    #authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        #生成账号的时候同时返回token
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()




from django.shortcuts import render

# Create your views here.
from random import choice
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets
from .serializers import SmsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import VerifyCode

from utils.yunpian import YunPian
from FruitShop.settings import APIKEY


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






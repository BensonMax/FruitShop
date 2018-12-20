import requests
import json

class YunPian(object):
    """
    send sms
    """
    def __init__(self,api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "测试模板".format(code=code)
        }

        respone = requests.post(self.single_send_url,data = parmas)
        re_dict = json.loads(respone.text)
        return re_dict

if __name__ == "__main__":
    yun_pian = YunPian("12312312312312")
    yun_pian.send_sms("2017","13763321011")




from api.base_api import BaseApi

class WeWork(BaseApi):


    def get_token(self,corpsecret):
        corpid ="wwe2b87cba46fecb13"
        corpsecret = corpsecret
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }

        #获取token
        res = self.send(data)
        token = res.json()['access_token']
        return token


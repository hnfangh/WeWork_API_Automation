
from api.base_api import BaseApi
from api.wework_token import WeWork


class Address(BaseApi):

    def __init__(self):
        self.corpsecret = "zXw69_DpO8A77XI6hgDKFV58So0eXdiLPhJL3KwLrOk"
        self.token = WeWork().get_token(self.corpsecret)


    # 创建成员
    def create_contacts(self,userid, name, mobile):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {
                "access_token": self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": [1]
            }
        }
        res = self.send(data)
        return res.json()

    # 获取成员
    def get_contacts(self,userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        res = self.send(data)
        return res.json()

    # 更新成员
    def update_contacts(self,userid, name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "json": {
                "userid": userid,
                "name": name,
                "department": [1]
            },
            "params": {
                "access_token": self.token
            }
        }
        res = self.send(data)
        return res.json()

    # 删除成员
    def delete_contacts(self,userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        res = self.send(data)
        return res.json()




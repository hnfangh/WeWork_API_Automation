import requests

class BaseApi:

    def send(self,data):
        res = requests.request(**data)
        return res


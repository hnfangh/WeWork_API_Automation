
# 企业微信API_Automation

## APIObject

    - api 基础API目录
        base_api.py 封装基础request封装，**data传参以字典形式解包
        token.py 封装通用token的获取
        address.py 业务功能添加企微成员信息类，具体业务功能实现
        
    - testcase 测试用例的目录
        test_address.py 测试具体的业务方法并断言

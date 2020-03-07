# -*- coding: utf-8 -*-
import requests,json,jsonpath
class HTTP:
     def __init__(self):
         self.session = requests.session()
         self.result = ''
         self.jsonres = {}
         self.params = {}

     def post(self,url,d=None,j=None,en='utf8'):
         # if d is None:
         #     pass
         # else:
         #     d = self.__get_data(d)
         res = self.session.post(url,d,j)
         self.result = res.content.decode(en)
         self.jsonres = json.loads(self.result)
         jsons = self.result
         jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]
         self.jsonres = json.loads(jsons)

     def addheader(self,key,value):
         value = self.__get_params(value)
         self.session.headers[key] = value

     def assertequals(self, jpath, value):
         """
         断言json结果里面，某个键的值和value相等
         :param key: json结果的键
         :param value: 预期的值
         :return: 无
         """
         value = self.__get_param(value)
         res = str(self.result)
         try:
             res = str(jsonpath.jsonpath(self.jsonres, jpath)[0])
         except Exception as e:
             pass

     def savejson(self,jpath,p):
         self.params[p] = str(jsonpath.jsonpath(self.jsonres,jpath)[0])

     def __get_params(self,s):
         #s = ''
         for key in self.params:
             s = s.replace('{'+key+'}',self.params[key])

             return s

     def __get_data(self, s):
         # 默认是标准的url参数
         flg = False
         # s = eval(s)
         # return s
         # 分离键值对
         param = {}
         p = s.split('&')
         # 获取键和值
         # username=Roy&password
         for pp in p:
             # 分离键和值
             ppp = pp.split('=')
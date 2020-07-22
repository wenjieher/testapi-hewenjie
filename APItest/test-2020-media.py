import json
import requests
import time

# 正确的用户名&正确的密码登陆

url = "https://hongkou-gateway.shmedia.tech/api/authority/verification/login"

payload = "{\"username\": \"hwj\", \"password\": \"Wdit@123\"}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
res = json.loads(response.text)
accessToken = res["data"]["access_token"]
if res['msg'] == '处理成功':
    print('登陆pass')
else:
    print('登陆fail')

# 获取用户信息
url = "https://hongkou-gateway.shmedia.tech/api/authority/user/getUserInfo"

headers = {
    'Content-Type': "application/json",
    'accessToken': accessToken
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == '处理成功':
    print('用户信息获取pass')
else:
    print('用户信息获取fail')

# 首页获取统计数据
url = "https://hongkou-gateway.shmedia.tech/api/port/workbench/statistic"

headers = {
    'Content-Type': "application/json",
    'accessToken': accessToken
    }
response = requests.request("POST", url, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'success':
    print('首页统计数据获取pass')
else:
    print('首页统计数据获取fail')


# 新建线索
url = "https://hongkou-gateway.shmedia.tech/api/interview/clue/add/clue"

payload = "{\"title\":\"test\",\"content\":\"test\",\"status\": 0}"
headers = {
            'Content-Type': 'application/json',
            'accessToken': accessToken
        }

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
res = json.loads(response.text)
c = res["data"]["id"]
if res['msg'] == 'success':
    print('新建线索pass')
else:
    print('新建线索fail')


# 提交线索



# -*- coding: utf-8 -*-
import json
import requests
import time

# 正确的用户名&正确的密码登陆

result = requests.post("https://test.shmedia.tech/api/authority/verification/login",
                       data={'username': 'hwjzongbian','password': 'Wdit@123'})
jsonres = json.loads(result.text)
print(result.text)
accessToken = jsonres["data"]["access_token"]
if jsonres['msg'] == '处理成功':
    print('登陆pass')
else:
    print('登陆fail')

# 获取用户信息
url = "https://test.shmedia.tech/api/authority/user/getUserInfo"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
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
url = "https://test.shmedia.tech/api/interview/data/statistic/get/wholeIndexStatistic"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken
    }
response = requests.request("POST", url, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('首页统计数据获取pass')
else:
    print('首页统计数据获取fail')

# 首页获取采访列表
url = "https://test.shmedia.tech/api/interview/mission/get/dealtInterviewList"

payload = {'PageNo':'1',
           'PageSize':'99'}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('首页采访列表获取pass')
else:
    print('首页采访列表获取fail')

# 线索列表
url = "https://test.shmedia.tech/api/interview/clue/get/pageList"

payload = "%08pageNo=1&pageSize=5&deptIds=&endDate=&hasMedia=&isPrivate=&keywords=&orderBy=&originIds=&searchOption=&startDate=&status=&tagIds=&type="
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    'cache-control': "no-cache",
    'Postman-Token': "c85fa76e-9ef2-4b8b-b155-ec196507e0d7"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('线索列表获取pass')
else:
    print('线索列表获取fail')

# 新建线索
url = "https://test.shmedia.tech/api/interview/clue/add/clue"

payload = "contentType=0&status=0&deptId=1&originId=1123c4a3sfdfdfds2e8f724bb8bd2dsfd&title=2%E5%8F%B7%E7%BA%BF8%E7%BC%96%E5%88%97%E8%BD%A6%E7%9B%B4%E9%80%9A%E6%B5%A6%E4%B8%9C%E6%9C%BA%E5%9C%BA%20%E9%99%A4%E6%97%A9%E9%AB%98%E5%B3%B0%E5%B9%BF%E5%85%B0%E8%B7%AF%E7%AB%99%E6%8D%A2%E4%B9%98&content=2%E5%8F%B7%E7%BA%BF8%E7%BC%96%E5%88%97%E8%BD%A6%E7%9B%B4%E9%80%9A%E6%B5%A6%E4%B8%9C%E6%9C%BA%E5%9C%BA%20%E9%99%A4%E6%97%A9%E9%AB%98%E5%B3%B0%E5%A4%96%E6%97%A0%E9%9C%80%E5%9C%A8%E5%B9%BF%E5%85%B0%E8%B7%AF%E7%AB%99%E6%8D%A2%E4%B9%98&pushIds=1%2C2&author=11&originUrl=www.baidu.com&tags=%E5%9C%B0%E9%93%81&reportSpeed=300&remarks=%E6%B5%8B%E8%AF%95%E5%A4%87%E6%B3%A8&interviewIds=11&imageList=%5B%7B%22attachPath%22%3A619949%2C%22attachName%22%3A%22%E8%BF%9B%E5%8D%9A.jpg%22%7D%5D"
headers = {
    'accessToken': accessToken,
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "afb97ec5-b50f-4981-ad94-2156a9a8145b"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
res = json.loads(response.text)
c = res["data"]["id"]
if res['msg'] == 'OK':
    print('新建线索pass')
else:
    print('新建线索fail')

# 线索详情
url = "https://test.shmedia.tech/api/interview/clue/get/clue"
payload = {'clueId': c}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    'cache-control': "no-cache",
    'Postman-Token': "dc5eccee-2885-42b2-ae07-d68b9d6dfe26"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('获取线索详情pass')
else:
    print('获取线索详情fail')

# 提交线索
url = "https://test.shmedia.tech/api/interview/clue/update/uploadStatus"

payload = {'clueId': c}
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'accessToken': accessToken,
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "fb307b16-36e9-4284-bd24-bd5489a55b7a"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('提交线索pass')
else:
    print('提交线索fail')

# 新建发布选题
url = "https://test.shmedia.tech/api/interview/topic/add/topic"

payload ={'title': '选题2号线8编列车直通浦东机场',
          'content':'选题关联线索2号线8编列车直通浦东机场',
          'status':'0',
          'tags':'地铁',
          'remarks':'无',
          'reportIds':'',
          'interviewIds':'',
          'pushIds':'',
          'clueIds':c
          }
headers = {

    'accessToken': accessToken

    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
topicid = res["data"]["id"]
if res['msg'] == 'OK':
    print('新建选题pass')
else:
    print('新建选题fail')

# 发布选题
url = "https://test.shmedia.tech/api/interview/topic/update/publishStatus"

payload = {"topicIds" : topicid}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
if res['msg'] == 'OK':
    print('发布选题pass')
else:
    print('发布选题fail')

# 选题列表
url = "https://test.shmedia.tech/api/interview/topic/get/pageList"

payload = "pageNo=1&pageSize=5"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    'cache-control': "no-cache",
    'Postman-Token': "43925f44-81eb-4c2b-b722-ca4d624d0f7c"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('选题列表获取pass')
else:
    print('选题列表获取fail')
# 新建采访
url = "https://test.shmedia.tech/api/interview/mission/add/interview"

payload = {'title':'[采访]互学互鉴进一步深化合作交流',
           'deptId':'05e8d463721b4c1b91810540bf3eeb3d',
           'deptName':'采访部',
           'startTime':'2019-05-22 14:42:24',
           'endTime':'2019-05-22 18:42:24',
           'address':'上海市浦东新区张江镇由心咖啡(张江盛大天地店)盛大天地青春里',
           'remarks':'无',
           'baseClass':'司机#1',
           'subClass':'摄像机#1',
           'reporters':'47033479ef3b48eeaad6100d3875f295',
           'status':'0',
           'topicId':'bc91aab5ea004a619d1cedff2f7b0461'}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    'cache-control': "no-cache",
    'Postman-Token': "b784fa5b-9d71-4c43-9c56-b8308dfd69f7"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
res = json.loads(response.text)
d = res["data"]["id"]
if res['msg'] == 'OK':
    print('新建采访pass')
else:
    print('新建采访fail')

# 采访列表
url = "https://test.shmedia.tech/api/interview/mission/get/pageList"

payload = {'PageNo':1,
           'PageSize':10}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    'cache-control': "no-cache",
    'Postman-Token': "e4f25349-9b02-4b91-b6c9-f102c21719cb"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('获取采访列表pass')
else:
    print('获取采访列表fail')

# 派发采访
url = "https://test.shmedia.tech/api/interview/mission/update/batchAuditStatus"

payload = {'interviewId':d}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('派发采访pass')
else:
    print('派发采访fail')

# 送审
url = "https://test.shmedia.tech/api/interview/mission/update/publishStatus"

payload = {'interviewId': d}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('采访送审pass')
else:
    print('采访送审fail')

# 审核
url = "https://test.shmedia.tech/api/interview/mission/update/batchAuditStatus"

payload = {'interviewIds': d,
          'operation':'0'}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('采访审核pass')
else:
    print('采访审核fail')

# 创建报道
url = "https://test.shmedia.tech/api/interview/report/add/report"

payload = {'title':'[报道]互学互鉴进一步深化合作交流合作',
           'content':'互学互鉴进一步深化合作交流',
           'deptId':'05e8d463721b4c1b91810540bf3eeb3d',
           'interviewIds':d,
           'status':'0',
           'imageList':'[{"attachPath":679084,"attachName":"9.jpg"}]',
           'contentType':'0',
           'reporters':'47033479ef3b48eeaad6100d3875f295',
           }
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    'cache-control': "no-cache",
    'Postman-Token': "5b61ce2b-d772-4fb7-af9f-957cb48ad013"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
e = res["data"]["id"]
if res['msg'] == 'OK':
    print('创建报道pass')
else:
    print('创建报道fail')

# 报道送审
url = "https://test.shmedia.tech/api/interview/report/update/submitStatus"

payload = {'reportId':e}
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    'cache-control': "no-cache",
    'Postman-Token': "04ce48af-1373-468e-a26d-b481849d96c9"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('报道送审pass')
else:
    print('报道送审fail')

# 审核报道
url = "https://test.shmedia.tech/api/interview/report/update/auditStatus"

payload = {'ids':e,
           'operation':'0'
           }
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    'cache-control': "no-cache",
    'Postman-Token': "76f7ff56-c4c3-4a24-9326-94b501911ec2"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('报道审核pass')
else:
    print('报道审核fail')

# 报道列表
url = "https://test.shmedia.tech/api/interview/report/get/pageList"

payload = {'pageNo':'1',
           'pageSize':'10'}
headers = {
    'accessToken': accessToken,
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "aa4d09ee-d430-4f40-9322-a34a6f2ba01e"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('获取报道列表pass')
else:
    print('获取报道列表fail')

# 推送报道
url = "https://test.shmedia.tech/api/interview/report/push/report"

payload = {'reportIdList':e,
           'pushes':'[{"pushId":"18-app","pushName":"APP","channelList":[{"channelId":"cd523e625af84ac3a7aeaf21b5e7d946","channelName":"生活"}]}]'}
headers = {
    'accessToken': accessToken,
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "c3254261-3d98-4c74-abad-0f4e4b799348"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('推送报道pass')
else:
    print('推送报道fail')

# 获取发布列表第一条
url = "https://test.shmedia.tech/api/jingle/cms/content/list"

payload = "pageNo=1&pageSize=1&channelId=cd523e625af84ac3a7aeaf21b5e7d946&orderBy="
headers = {
    'accessToken': accessToken,
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
res = json.loads(response.text)
f = res["data"]["records"][0]["id"]
print(f)
if res['msg'] == 'OK':
    print('获取发布第一条pass')
else:
    print('获取发布第一条fail')

# 提交发布审核
url = "https://test.shmedia.tech/api/jingle/cms/content/check"

payload = {'ids':f}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken,
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('提交发布审核pass')
else:
    print('提交发布审核fail')

# 一审
url = "https://test.shmedia.tech/api/jingle/cms/content/check"

payload = {'ids':f}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken

    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('一审pass')
else:
    print('一审fail')

# 二审
url = "https://test.shmedia.tech/api/jingle/cms/content/check"

payload = {'ids':f}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken

    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('二审pass')
else:
    print('二审fail')

# 三审发布
url = "https://test.shmedia.tech/api/jingle/cms/content/check"

payload = {'ids':f}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'accessToken': accessToken

    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
res = json.loads(response.text)
if res['msg'] == 'OK':
    print('三审发布pass')
else:
    print('三审发布fail')


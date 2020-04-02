import requests,json
import time
#徐汇
#新闻稿件详情
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'16',
           'linkType':'1',
           'contentId':'f1961d5cdd3f41bf8f7c94a4e8fe9cc9',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'https://test.shmedia.tech/app_xh/xh_sz/20191231/1d041d40f7dd47138e6f29b867c6c8d9.html?from=singlemessage',
           'title':'新闻：金句之七：伟大出自平凡 平凡造就伟大',
           'content':'金句之七：伟大出自平凡 平凡造就伟大',
           'titleImage':'',
           'releaseDate':'',
           'channelName':'',
           'hotspotName':'',
           'attrs':'',
           'letterFlg':'1'
           }
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
dd = response.json()['data']
print(dd)

url = "http://192.168.230.17:9003/media-basic-community/api/messagePush/systemMessage"

payload = {'id' : dd}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",

    }

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
time.sleep(3)
#外链
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'16',
           'linkType':'6',
           'contentId':'',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'https://test.shmedia.tech/app_xh/xh_sz/20191231/1d041d40f7dd47138e6f29b867c6c8d9.html?from=singlemessage',
           'title':'外链：金句之七：伟大出自平凡 平凡造就伟大',
           'content':'金句之七：伟大出自平凡 平凡造就伟大',
           'titleImage':'',
           'releaseDate':'',
           'channelName':'',
           'hotspotName':'',
           'attrs':'',
           'letterFlg':'1'
           }
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
dd = response.json()['data']
print(dd)

url = "http://192.168.230.17:9003/media-basic-community/api/messagePush/systemMessage"

payload = {'id' : dd}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",

    }

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
time.sleep(3)

#图集
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'16',
           'linkType':'5',
           'contentId':'2ed8a5ede45344f7b968de58a0d083c8',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'https://test.shmedia.tech/app_xh/xh_tj/20191031/2f8c9e67d02e42aebdacdc1111a62cfc.html',
           'title':'图集：金句之七：伟大出自平凡 平凡造就伟大',
           'content':'金句之七：伟大出自平凡 平凡造就伟大',
           'titleImage':'',
           'releaseDate':'',
           'channelName':'',
           'hotspotName':'',
           'attrs':'',
           'letterFlg':'1'
           }
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
dd = response.json()['data']
print(dd)

url = "http://192.168.230.17:9003/media-basic-community/api/messagePush/systemMessage"

payload = {'id' : dd}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",

    }

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
time.sleep(3)

#专题列表
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'16',
           'linkType':'2',
           'contentId':'',
           'channelType':'',
           'channelId':'338fab2fba5a4fe7a51983f4702b52bd',
           'subChannelId':'52386129eedb4591a54a4025f0bb5eab',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'',
           'title':'专题列表：金句之七：伟大出自平凡 平凡造就伟大',
           'content':'金句之七：伟大出自平凡 平凡造就伟大',
           'titleImage':'',
           'releaseDate':'',
           'channelName':'',
           'hotspotName':'',
           'attrs':'',
           'letterFlg':'1'
           }
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
dd = response.json()['data']
print(dd)

url = "http://192.168.230.17:9003/media-basic-community/api/messagePush/systemMessage"

payload = {'id' : dd}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",

    }

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
time.sleep(3)

#专题详情
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'16',
           'linkType':'3',
           'contentId':'93a458eda8ca413e9b26c0860f88259f',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'https://test.shmedia.tech/app_xh/zttest/20191101/5a0ccd8e65cc418e83810d86f585768c.html',
           'title':'专题：金句之七：伟大出自平凡 平凡造就伟大',
           'content':'金句之七：伟大出自平凡 平凡造就伟大',
           'titleImage':'',
           'releaseDate':'',
           'channelName':'',
           'hotspotName':'',
           'attrs':'',
           'letterFlg':'1'
           }
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
dd = response.json()['data']
print(dd)

url = "http://192.168.230.17:9003/media-basic-community/api/messagePush/systemMessage"

payload = {'id' : dd}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",

    }

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
time.sleep(3)

#视频原生
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'16',
           'linkType':'4',
           'contentId':'d51e19183b0c4ed6b1e7069289c88af1',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'',
           'title':'视频：金句之七：伟大出自平凡 平凡造就伟大',
           'content':'金句之七：伟大出自平凡 平凡造就伟大',
           'titleImage':'',
           'releaseDate':'',
           'channelName':'',
           'hotspotName':'',
           'attrs':'',
           'letterFlg':'1'
           }
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
dd = response.json()['data']
print(dd)

url = "http://192.168.230.17:9003/media-basic-community/api/messagePush/systemMessage"

payload = {'id' : dd}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",

    }

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
time.sleep(3)

#文本
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'16',
           'linkType':'7',
           'contentId':'',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'',
           'title':'文本：金句之七：伟大出自平凡 平凡造就伟大',
           'content':'金句之七：伟大出自平凡 平凡造就伟大',
           'titleImage':'',
           'releaseDate':'',
           'channelName':'',
           'hotspotName':'',
           'attrs':'',
           'letterFlg':'1'
           }
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
dd = response.json()['data']
print(dd)

url = "http://192.168.230.17:9003/media-basic-community/api/messagePush/systemMessage"

payload = {'id' : dd}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",

    }

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
time.sleep(3)

#直播列表
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'16',
           'linkType':'12',
           'contentId':'',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'',
           'title':'直播列表：金句之七：伟大出自平凡 平凡造就伟大',
           'content':'金句之七：伟大出自平凡 平凡造就伟大',
           'titleImage':'',
           'releaseDate':'',
           'channelName':'',
           'hotspotName':'',
           'letterFlg':'1',
           'attrs':'{"url":"http://test.shmedia.tech/live/index.html#/details/10","isShared":"0","live_type":"2_list"}'
           }
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
dd = response.json()['data']
print(dd)

url = "http://192.168.230.17:9003/media-basic-community/api/messagePush/systemMessage"

payload = {'id' : dd}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",

    }

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
time.sleep(3)

#直播
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'16',
           'linkType':'12',
           'contentId':'',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'',
           'title':'直播：金句之七：伟大出自平凡 平凡造就伟大',
           'content':'金句之七：伟大出自平凡 平凡造就伟大',
           'titleImage':'',
           'releaseDate':'',
           'channelName':'',
           'hotspotName':'',
           'letterFlg':'1',
           'attrs':'{"url":"http://test.shmedia.tech/live/index.html#/details/10","isShared":"0","live_type":"2","roomId":"c1b25b92-66dc-4454-aee0-a5f65f18ad6f"}'
           }
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
dd = response.json()['data']
print(dd)

url = "http://192.168.230.17:9003/media-basic-community/api/messagePush/systemMessage"

payload = {'id' : dd}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",

    }

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text)
time.sleep(3)
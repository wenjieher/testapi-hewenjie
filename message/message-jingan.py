import requests,json
import time
#静安
#新闻稿件详情
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'24',
           'linkType':'1',
           'contentId':'e5ceadd116444642a82f57f0bccd8e82',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'https://test.shmedia.tech/app_bs/bs_tj/20191205/3751dad8725144b198a8bfce4931741e.html?from=singlemessage',
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
payload = {'siteId':'24',
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
payload = {'siteId':'24',
           'linkType':'5',
           'contentId':'c614f39fd86d49c0a4c0d4c379dd2935',
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
payload = {'siteId':'24',
           'linkType':'2',
           'contentId':'',
           'channelType':'',
           'channelId':'c2da4b3ee63740738e36d29621500796',
           'subChannelId':'29b1072e7d5643f1a7db229891c22e04',
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
payload = {'siteId':'24',
           'linkType':'3',
           'contentId':'e5ceadd116444642a82f57f0bccd8e82',
           'channelType':'',
           'channelId':'',
           'subChannelId':'',
           'terminalChannelId':'',
           'hotspotId':'',
           'url':'https://test.shmedia.tech/app_bs/bs_zt-yq/20200130/4b7ce79b276c4017a8f41d1437406180.html?from=singlemessage',
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
payload = {'siteId':'24',
           'linkType':'4',
           'contentId':'c72e03df689040029e68f02b593ef3f8',
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
payload = {'siteId':'24',
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
payload = {'siteId':'24',
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
payload = {'siteId':'24',
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
import requests,json
import time
#静安
#新闻稿件详情
url = "http://192.168.230.17:9003/media-basic-community/api/member/pushContent/insertSystemMessage"
payload = {'siteId':'21',
           'linkType':'1',
           'contentId':'0563bc635a5641bfac8a230cc82e1102',
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
payload = {'siteId':'21',
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
payload = {'siteId':'21',
           'linkType':'5',
           'contentId':'d364b8d4571d4e02bf050ed507ea6ade',
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
payload = {'siteId':'21',
           'linkType':'2',
           'contentId':'',
           'channelType':'',
           'channelId':'d8a270d59aae4085b12406b535e4fcc0',
           'subChannelId':'f34aa36f685e4dd69b22e4b3d769795f',
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
payload = {'siteId':'21',
           'linkType':'3',
           'contentId':'94857af331c249a68e451c242080471b',
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
payload = {'siteId':'21',
           'linkType':'4',
           'contentId':'01f27aa9216a41d593679cf16b306578',
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
payload = {'siteId':'21',
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
payload = {'siteId':'21',
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
payload = {'siteId':'21',
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
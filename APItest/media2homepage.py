# -*-coding：UTF:8-*-
import unittest
import json,requests

class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.session = requests.session()
        s = self.session.post("http://k8s.shmedia.tech/api/authority/verification/login",data="{\"username\":\"hwjzongbian\",\"password\":\"Wdit@123\"}",headers = {'Content-Type': 'application/json'})
        #self.jsonres = json.loads(s.text)
        self.access_Token = s.json()["data"]["access_token"]
        c = self.session.post("http://k8s.shmedia.tech/api/interview/clue/add/clue", data="{\"content\":\"<p>content</p>\",\"title\":\"test\",\"originId\":\"1123c4a3sfdfdfds2e8f724bb8bd2dsfd\",\"imageList\":[{\"attachName\":\"81f8a509gy1fnjdvkkwgoj20zk0m8ak8.jpg\",\"attachPath\":\"0443b67b9ca74b4b869c805941cddbf5\"}],\"status\":\"0\"}", headers={'Content-Type': 'application/json','accessToken': self.access_Token})
        # self.jsonres = json.loads(s.text)
        self.clueid = c.json()["data"]["id"]
        print(self.clueid)
        t = self.session.post("http://k8s.shmedia.tech/api/interview/clue/add/clue", data="{\"content\":\"<p>content</p>\",\"title\":\"test\",\"originId\":\"1123c4a3sfdfdfds2e8f724bb8bd2dsfd\",\"imageList\":[{\"attachName\":\"81f8a509gy1fnjdvkkwgoj20zk0m8ak8.jpg\",\"attachPath\":\"0443b67b9ca74b4b869c805941cddbf5\"}],\"status\":\"0\"}", headers={'Content-Type': 'application/json', 'accessToken': self.access_Token})
        # self.jsonres = json.loads(s.text)
        self.clueid = c.json()["data"]["id"]

    @classmethod
    def tearDown(self):
        print('****************end*****************')


    def test001(self):
        """新建线索"""

        url = "http://k8s.shmedia.tech/api/interview/clue/add/clue"

        payload = "{\"content\":\"<p>content</p>\",\"title\":\"test\",\"originId\":\"1123c4a3sfdfdfds2e8f724bb8bd2dsfd\",\"imageList\":[{\"attachName\":\"81f8a509gy1fnjdvkkwgoj20zk0m8ak8.jpg\",\"attachPath\":\"0443b67b9ca74b4b869c805941cddbf5\"}],\"status\":\"0\"}"
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)


    def test002(self):
        """提交线索"""

        url = "http://k8s.shmedia.tech/api/interview/clue/update/batchUploadStatus"

        payload = self.clueid
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=[payload])
        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test003(self):
        """新建选题"""

        url = "http://k8s.shmedia.tech/api/interview/topic/add/topic"

        payload = "{\n    \"title\": \"topictitle\",\n    \"content\": \"<p>topiccontent容</p>\",\n    \"originUrl\": \"https://www.baidu.com\",\n    \"address\": \"http://www.shanghai.gov.cn/shanghai/n46669/n48081/u22ai129215.html\",\n    \"startTime\": \"2020-05-26 02:16:01\",\n    \"endTime\": \"2020-05-31 02:16:04\",\n    \"imageList\": [\n        {\n            \"attachName\": \"81f8a509gy1fnjdvkkwgoj20zk0m8ak8.jpg\",\n            \"attachPath\": \"0443b67b9ca74b4b869c805941cddbf5\"\n        }\n    ],\n    \"clueIds\": \"7110407049634d36ad1000a19a728c9b\",\n    \"photo\": \"https://70test.storage.shmedia.tech/1153474.png\",\n    \"status\": \"0\"\n}"
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=[payload])
        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        topicid = response.json()['data']['id']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)




if __name__ == '__main__':
    unittest.main()
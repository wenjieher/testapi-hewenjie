# -*-coding：UTF:8-*-
import unittest
import json,requests

class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.session = requests.session()
        s = self.session.post("https://hongkou-gateway.shmedia.tech/api/authority/verification/login",data="{\"username\":\"hwj\",\"password\":\"Wdit@123\"}",headers = {'Content-Type': 'application/json'})
        #self.jsonres = json.loads(s.text)
        self.access_Token = s.json()["data"]["access_token"]
        c = self.session.post("https://hongkou-gateway.shmedia.tech/api/interview/clue/add/clue", data="{\"title\":\"test clue\",\"content\":\"<p>test</p>\",\"status\":\"0\"}", headers={'Content-Type': 'application/json','accessToken': self.access_Token})
        # self.jsonres = json.loads(s.text)
        self.clueid = c.json()["data"]["id"]
        print(self.clueid)
        t = self.session.post("https://hongkou-gateway.shmedia.tech/api/interview/topic/add/topic", data="{\"title\":\"new topic\",\"content\":\"<p>topic</p>\",\"startTime\":\"2020-07-22 11:21:00\",\"endTime\":\"2020-07-29 11:21:00\",\"clueIds\":\"\",\"photo\":\"https://wdit.storage.shmedia.tech/225295.jpg\",\"status\":\"0\"}", headers={'Content-Type': 'application/json','accessToken': self.access_Token})
        self.topicid = t.json()["data"]["id"]
        task = self.session.post("https://hongkou-gateway.shmedia.tech/api/interview/mission/add/newInterview", data="{\"title\":\"test task\",\"startTime\":\"2020-07-22 13:54:00\",\"endTime\":\"2021-07-21 13:54:00\",\"remarks\":\"<p>task</p>\",\"longitude\":\"\",\"latitude\":\"\",\"subClass\":\"&#x91C7;&#x8BBF;&#x8F66;#0,&#x5355;&#x53CD;&#x76F8;&#x673A;#0,&#x6444;&#x50CF;&#x673A;#0,&#x84DD;&#x5149;&#x76F8;&#x673A;#0,&#x673A;&#x67B6;#0,&#x4FBF;&#x643A;DV#0,&#x5168;&#x5A92;&#x4F53;&#x5305;#0,&#x8BDD;&#x7B52;#0,&#x5C0F;&#x871C;&#x8702;#0,&#x5F55;&#x97F3;&#x7B14;#0,&#x79FB;&#x52A8;&#x975E;&#x7F16;#0\",\"topicId\":\"\",\"interviewReporterVoList\":[{\"reporterId\":\"baa955cfba9a458cbbe2e9aa197cd274\",\"reporterName\":\"&#x4F55;&#x6587;&#x6770;\",\"photo\":\"https://wdit.storage.shmedia.tech/225295.jpg\",\"type\":\"1\"}],\"status\":\"6\"}", headers={'Content-Type': 'application/json', 'accessToken': self.access_Token})
        self.taskid = task.json()["data"]["id"]
        task1 = self.session.post("https://hongkou-gateway.shmedia.tech/api/interview/mission/add/newInterview",data="{\"title\":\"test task\",\"startTime\":\"2020-07-22 13:54:00\",\"endTime\":\"2021-07-21 13:54:00\",\"remarks\":\"<p>task</p>\",\"longitude\":\"\",\"latitude\":\"\",\"subClass\":\"&#x91C7;&#x8BBF;&#x8F66;#0,&#x5355;&#x53CD;&#x76F8;&#x673A;#0,&#x6444;&#x50CF;&#x673A;#0,&#x84DD;&#x5149;&#x76F8;&#x673A;#0,&#x673A;&#x67B6;#0,&#x4FBF;&#x643A;DV#0,&#x5168;&#x5A92;&#x4F53;&#x5305;#0,&#x8BDD;&#x7B52;#0,&#x5C0F;&#x871C;&#x8702;#0,&#x5F55;&#x97F3;&#x7B14;#0,&#x79FB;&#x52A8;&#x975E;&#x7F16;#0\",\"topicId\":\"\",\"interviewReporterVoList\":[{\"reporterId\":\"baa955cfba9a458cbbe2e9aa197cd274\",\"reporterName\":\"&#x4F55;&#x6587;&#x6770;\",\"photo\":\"https://wdit.storage.shmedia.tech/225295.jpg\",\"type\":\"1\"}],\"status\":\"1\"}",headers={'Content-Type': 'application/json', 'accessToken': self.access_Token})
        self.taskid1 = task1.json()["data"]["id"]
        a = self.session.post("https://hongkou-gateway.shmedia.tech/api/jingle/cms/organization-content/personal/add", data="{\"channelId\":null,\"modelId\":\"310109-1\",\"txt\":\"<p><span style=\\\"background-color: rgb(255, 255, 255); color: rgb(51, 51, 51);\\\">article</span></p>\",\"reporters\":[],\"title\":\"test article\",\"missions\":[],\"clues\":[],\"coverImages\":[],\"coverImageType\":\"multi-image\",\"link\":\"\"}", headers={'Content-Type': 'application/json', 'accessToken': self.access_Token})
        self.articleid = a.json()["data"]["id"]
        articlesend = self.session.post("https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/autoAdd", data="{\"modelId\":\"310109-1\",\"channelId\":\"b08f8f2bf3344bedb88217287907d9fc\",\"txt\":\"<p>test</p>\",\"lock\":false,\"settings\":{\"configUI\":{\"shortcuts\":{\"enable\":true},\"panels\":{\"enable\":true},\"comments\":{\"enable\":true},\"hasLogin\":{\"enable\":true},\"header\":{\"enable\":true,\"title\":\"\",\"close\":\"enable\",\"voice\":\"enable\",\"more\":\"enable\"},\"footer\":{\"enable\":true,\"input\":\"enable\",\"favorite\":\"enable\",\"like\":\"enable\"},\"moreBox\":{\"share\":\"enable\",\"theme\":\"enable\",\"report\":\"enable\",\"copyLink\":\"enable\"}},\"appConfig\":{\"hasLogin\":{\"enable\":false}},\"configShare\":{\"title\":\"\",\"summary\":\"\",\"link\":\"\",\"imageUrl\":\"\",\"imageId\":\"\"}},\"link\":\"\",\"coverImages\":[],\"coverImageType\":\"multi-image\",\"title\":\"test article send\"}", headers={'Content-Type': 'application/json', 'accessToken': self.access_Token})
        self.articlesend = articlesend.json()["data"]["id"]
        articledelete = self.session.post("https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/autoAdd",data="{\"modelId\":\"310109-1\",\"channelId\":\"b08f8f2bf3344bedb88217287907d9fc\",\"txt\":\"<p>test</p>\",\"lock\":false,\"settings\":{\"configUI\":{\"shortcuts\":{\"enable\":true},\"panels\":{\"enable\":true},\"comments\":{\"enable\":true},\"hasLogin\":{\"enable\":true},\"header\":{\"enable\":true,\"title\":\"\",\"close\":\"enable\",\"voice\":\"enable\",\"more\":\"enable\"},\"footer\":{\"enable\":true,\"input\":\"enable\",\"favorite\":\"enable\",\"like\":\"enable\"},\"moreBox\":{\"share\":\"enable\",\"theme\":\"enable\",\"report\":\"enable\",\"copyLink\":\"enable\"}},\"appConfig\":{\"hasLogin\":{\"enable\":false}},\"configShare\":{\"title\":\"\",\"summary\":\"\",\"link\":\"\",\"imageUrl\":\"\",\"imageId\":\"\"}},\"link\":\"\",\"coverImages\":[],\"coverImageType\":\"multi-image\",\"title\":\"test article send\"}",headers={'Content-Type': 'application/json', 'accessToken': self.access_Token})
        self.articledelete = articledelete.json()["data"]["id"]
        send = self.session.post("https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/page", data="{\"isDeleted\":false,\"recursion\":false,\"pageNo\":1,\"pageSize\":20,\"channelId\":\"b08f8f2bf3344bedb88217287907d9fc\"}",headers={'Content-Type': 'application/json', 'accessToken': self.access_Token})
        self.articleid1 = send.json()["data"]["records"][0]["id"]
        delete1 = self.session.post("https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/page", data="{\"isDeleted\":false,\"recursion\":false,\"pageNo\":1,\"pageSize\":20,\"channelId\":\"b08f8f2bf3344bedb88217287907d9fc\"}", headers={'Content-Type': 'application/json', 'accessToken': self.access_Token})
        self.delete1 = delete1.json()["data"]["records"][1]["id"]
        print(self.articleid1)

    @classmethod
    def tearDown(self):
        print('****************end*****************')

    def test001(self):
        """首页current-user/list接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/authority/admin/menu/current-user/list"

        payload = "{}"
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("处理成功", result1)
        self.assertEqual(0, result2)

    def test002(self):
        """首页user/getUserInfo接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/authority/user/getUserInfo"

        payload = {}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("处理成功", result1)
        self.assertEqual(0, result2)

    def test003(self):
        """首页personal/page接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/authority/inform/message/personal/page"

        payload = "{}"
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

    def test004(self):
        """首页todo/page接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/port/user/todo/page"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"ignore\":true,\"types\":[\"cms-content\",\"interview_interview\"]}"
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

    def test005(self):
        """首页workbench/statistic接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/port/workbench/statistic"

        payload = "{}"
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

    def test006(self):
        """首页/model/list接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/model/list"

        payload = "{}"
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

    def test007(self):
        """首页target/list接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/publish/target/list"

        payload = "{\"channelNeed\":true,\"enableFlag\":1}"
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

    def test008(self):
        """汇聚中心setting-group/all接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/gathering/setting-group/all"

        payload = "{\"channelNeed\":true,\"enableFlag\":1}"
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

    def test009(self):
        """汇聚中心get/pageList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/clue/get/pageList"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"orderBy\":3,\"type\":\"1\",\"isPrivate\":0,\"extraType\":\"310109-01\"}"
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

    def test010(self):
        """汇聚中心get/originList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/clueOrigin/get/originList"

        payload = "{\"type\":\"1\",\"extraType\":\"310109-01\"}"
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

    def test011(self):
        """汇聚中心-用户投稿get/pageList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/clue/get/pageList"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"orderBy\":3,\"type\":\"7\"}"
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text.encode)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test012(self):
        """线索管理get/pageList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/clue/get/pageList"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"orderBy\":3,\"isPrivate\":0}"
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

    def test013(self):
        """我的线索get/pageList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/clue/get/pageList"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"orderBy\":3,\"isPrivate\":1}"
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

    def test014(self):
        """新建线索add/clue接口"""

        url = "https://hongkou-gateway.shmedia.tech/api/interview/clue/add/clue"

        payload = "{\"title\":\"test clue\",\"content\":\"<p>test</p>\",\"status\":\"0\"}"
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

    def test015(self):
        """提交线索update/batchUploadStatus接口"""

        url = "https://hongkou-gateway.shmedia.tech/api/interview/clue/update/batchUploadStatus"

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

    def test016(self):
        """查看线索get/clue接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/clue/get/clue"

        payload = {'id':self.clueid}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test017(self):
        """选题管理列表topic/get/pageList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/topic/get/pageList"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"orderBy\":3,\"isPrivate\":0}"
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

    def test018(self):
        """新建选题add/topic接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/topic/add/topic"

        payload = "{\"title\":\"new topic\",\"content\":\"<p>topic</p>\",\"startTime\":\"2020-07-22 11:21:00\",\"endTime\":\"2020-07-29 11:21:00\",\"clueIds\":\"\",\"photo\":\"https://wdit.storage.shmedia.tech/225295.jpg\",\"status\":\"0\"}"
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

    def test019(self):
        """提交选题topic/update/publishStatus接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/topic/update/publishStatus"

        payload = [self.topicid]
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test020(self):
        """选题归档topic/update/batchIsHistory接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/topic/update/batchIsHistory"

        payload = [{'id':self.topicid,'isHistory':1}]
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test021(self):
        """还原归档选题update/batchIsHistory接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/topic/update/batchIsHistory"

        payload = [{'id':self.topicid,'isHistory':0}]
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)


    def test022(self):
        """我的选题topic/get/pageList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/topic/get/pageList"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"orderBy\":3,\"isPrivate\":1}"
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

    def test023(self):
        """新建任务add/newInterview接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/mission/add/newInterview"

        payload = "{\"title\":\"test task\",\"startTime\":\"2020-07-22 13:54:00\",\"endTime\":\"2021-07-21 13:54:00\",\"remarks\":\"<p>task</p>\",\"longitude\":\"\",\"latitude\":\"\",\"subClass\":\"采访车#0,单反相机#0,摄像机#0,蓝光相机#0,机架#0,便携DV#0,全媒体包#0,话筒#0,小蜜蜂#0,录音笔#0,移动非编#0\",\"topicId\":\"\",\"interviewReporterVoList\":[{\"reporterId\":\"baa955cfba9a458cbbe2e9aa197cd274\",\"reporterName\":\"何文杰\",\"photo\":\"https://wdit.storage.shmedia.tech/225295.jpg\",\"type\":\"1\"}],\"status\":\"6\"}"
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, data=payload.encode())

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test024(self):
        """提交任务update/sendInterview接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/mission/update/sendInterview"

        payload = [{'id':self.taskid}]
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test025(self):
        """撤销任务update/revokeInterview接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/mission/update/revokeInterview"

        payload = [{'id': self.taskid1}]
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test026(self):
        """领取任务update/drawInterview接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/mission/update/drawInterview"

        payload = [{'id': self.taskid}]
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test027(self):
        """派给我的get/pageList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/mission/get/pageList"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"orderBy\":\"createDate\",\"isPrivate\":1,\"showType\":1}"
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

    def test028(self):
        """我创建的任务get/pageList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/mission/get/pageList"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"orderBy\":\"createDate\",\"isPrivate\":1,\"showType\":0}"
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

    def test029(self):
        """归档列表get/pageList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/topic/get/pageList"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"orderBy\":3,\"isHistory\":1,\"status\":\"4\",\"isPrivate\":0}"
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

    def test030(self):
        """获取人员信息get/reporters接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/mission/get/reporters"

        payload = "{\"isCurrent\":true,\"deptId\":\"\"}"
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

    def test031(self):
        """获取选题详情get/topic接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/topic/get/topic"

        payload = {'id':self.topicid}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test032(self):
        """获取任务详情get/interview接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/interview/mission/get/interview"

        payload = {'id':self.taskid}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test033(self):
        """机构文稿列表organization-content/page接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/organization-content/page"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"isDeleted\":false,\"orderBy\":\"create_desc\"}"
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

    def test034(self):
        """获取我的文稿列表personal/page"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/organization-content/personal/page"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"isDeleted\":false,\"orderBy\":\"create_desc\",\"isPersonal\":null}"
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

    def test035(self):
        """新建文稿personal/add接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/organization-content/personal/add"

        payload = "{\"channelId\":null,\"modelId\":\"310109-1\",\"txt\":\"<p><span style=\\\"background-color: rgb(255, 255, 255); color: rgb(51, 51, 51);\\\">article</span></p>\",\"reporters\":[],\"title\":\"test article\",\"missions\":[],\"clues\":[],\"coverImages\":[],\"coverImageType\":\"multi-image\",\"link\":\"\"}"
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

    def test036(self):
        """提交文稿personal/submit接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/organization-content/personal/submit"

        payload = [{'id':self.articleid}]
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test037(self):
        """查看文稿personal/get接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/organization-content/personal/get"

        payload = {'id':self.articleid}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test038(self):
        """文稿取用渠道列表target/tree接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/publish/target/tree"

        payload = "{\"channelNeed\":true,\"enableFlag\":1,\"systemType\":1}"
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

    def test039(self):
        """取用到app栏目列表channel/list接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/publish/target/channel/list"

        payload = "{\"recursion\":true,\"targetId\":\"310109-1\",\"systemType\":\"1\"}"
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

    def test040(self):
        """文稿取用到apporganization-content/send接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/organization-content/send"

        payload = {'publishTargets':[{'id':'310109-1','channelList':[{'channelId':'b08f8f2bf3344bedb88217287907d9fc'}]}],'contents':[{'id':self.articleid}]}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test041(self):
        """机构文稿列表organization-content/page接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/organization-content/page"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"isDeleted\":false,\"orderBy\":\"create_desc\"}"
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

    def test042(self):
        """内容管理渠道列表target/tree接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/publish/target/tree"

        payload = "{\"enableFlag\":1,\"systemType\":2}"
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

    def test043(self):
        """内容管理列表content/page接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/page"

        payload = "{\"isDeleted\":false,\"recursion\":false,\"pageNo\":1,\"pageSize\":20,\"channelId\":\"b08f8f2bf3344bedb88217287907d9fc\"}"
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

    def test044(self):
        """文稿提交审核content/check接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/check"

        payload = {'contents':[{'id':self.articleid}]}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test045(self):
        """查看操作日志content/findEditRecordList接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/findEditRecordList"

        payload = "{\"channelContentId\":\"5ccbb0aa7095433ca9252a7462d0593f\"}"
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

    def test046(self):
        """查看审核日志record/list接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/workflow/record/list"

        payload = {'contentId':self.articleid}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test047(self):
        """提交文稿审核content/check接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/check"

        payload = {'contents':[{'id':self.articleid1}]}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test048(self):
        """发布审核列表content/page接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/page"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"status\":1,\"orderBy\":\"create_desc\"}"
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

    def test049(self):
        """一审content/check接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/check"

        payload = {'contents': [{'id': self.articleid1}]}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test050(self):
        """二审content/check接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/check"

        payload = {'contents': [{'id': self.articleid1}]}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test051(self):
        """三审发布content/check接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/check"

        payload = {'contents': [{'id': self.articleid1}]}
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test052(self):
        """获取评论管理列表review/list接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/external/article/review/list"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"sourceType\":\"2\",\"memberId\":\"\"}"
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

    def test053(self):
        """回收站列表content/page接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/page"

        payload = "{\"pageNo\":1,\"pageSize\":10,\"isDeleted\":true}"
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

    def test054(self):
        """删除草稿文稿content/delete接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/content/delete"

        payload = [{'id':self.delete1}]
        headers = {
            'Content-Type': 'application/json',
            'accessToken': 'dc755e05215bdd7e3648afe954116ee9'
        }

        response = requests.request("POST", url, headers=headers, json=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test055(self):
        """站点信息site/get接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/site/get"

        payload = "{}"
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

    def test056(self):
        """保存站点信息site/update信息"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/site/update"

        payload = "{\"id\":\"310109\",\"name\":\"虹口\",\"shortName\":\"虹口\",\"protocol\":\"https://\",\"domain\":\"hongkou-gateway.shmedia.tech\",\"releasePath\":\"/public/app_hk\",\"path\":\"app_hk\",\"staticSuffix\":\".html\",\"workflowId\":\"ID_27_001\",\"afterCheckFlag\":\"0\",\"recycleFlag\":\"1\",\"staticFlag\":\"1\",\"deleted\":false}"
        headers = {
            'Content-Type': 'application/json',
            'accessToken': self.access_Token
        }

        response = requests.request("POST", url, headers=headers, data=payload.encode())

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)

    def test057(self):
        """栏目管理列表channel/list接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/channel/list"

        payload = "{\"recursion\":true,\"parentId\":\"310109-3\"}"
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

    def test058(self):
        """模型管理model/list接口"""
        url = "https://hongkou-gateway.shmedia.tech/api/jingle/cms/model/list"

        payload = "{}"
        headers = {
            'Content-Type': 'application/json',
            'accessToken': 'dc755e05215bdd7e3648afe954116ee9'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        result1 = response.json()['msg']
        result2 = response.json()['code']
        print(result1)
        self.assertEqual("success", result1)
        self.assertEqual(0, result2)















if __name__ == '__main__':
    unittest.main()
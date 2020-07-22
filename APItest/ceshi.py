#coding=utf-8
import requests
task1 = post("https://hongkou-gateway.shmedia.tech/api/interview/mission/add/newInterview",
             data="{\"title\":\"test task\",\"startTime\":\"2020-07-22 13:54:00\",\"endTime\":\"2021-07-21 13:54:00\",\"remarks\":\"<p>task</p>\",\"longitude\":\"\",\"latitude\":\"\",\"subClass\":\"采访车#0,单反相机#0,摄像机#0,蓝光相机#0,机架#0,便携DV#0,全媒体包#0,话筒#0,小蜜蜂#0,录音笔#0,移动非编#0\",\"topicId\":\"\",\"interviewReporterVoList\":[{\"reporterId\":\"baa955cfba9a458cbbe2e9aa197cd274\",\"reporterName\":\"何文杰\",\"photo\":\"https://wdit.storage.shmedia.tech/225295.jpg\",\"type\":\"1\"}],\"status\":\"1\"}",
             headers={'Content-Type': 'application/json', 'accessToken': '3a4d08d49fd144d8962c8ae9762b84bf'})


# -*- coding: utf-8 -*-
import requests,json

def vip_get_token():
    test_url = 'http://k8s.shmedia.tech/api/authority/verification/login'
    test_data = "{\"username\":\"hwjzongbian\",\"password\":\"Wdit@123\"}"
    headers = {
        'Content-Type': 'application/json'
    }
    test_resp = requests.post(test_url, data=test_data, headers=headers)
    print(test_resp.text)
    token = test_resp.json()["data"]["access_token"]
    return token

def get_clueid():
    test_url = 'http://k8s.shmedia.tech/api/interview/clue/add/clue'
    test_data = "{\"content\":\"<p>content</p>\",\"title\":\"test\",\"originId\":\"1123c4a3sfdfdfds2e8f724bb8bd2dsfd\",\"imageList\":[{\"attachName\":\"81f8a509gy1fnjdvkkwgoj20zk0m8ak8.jpg\",\"attachPath\":\"0443b67b9ca74b4b869c805941cddbf5\"}],\"status\":\"0\"}"
    headers = {
        'Content-Type': 'application/json',
        'accessToken': vip_get_token()
    }
    test_resp = requests.post(test_url, data=test_data, headers=headers)
    print(test_resp.text)
    clueid = test_resp.json()["data"]["id"]
    return clueid

if __name__ == '__main__':
    print(vip_get_token())
    print(get_clueid())
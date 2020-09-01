# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# 写成了一个通用的函数接口，想直接用的话，把参数的注释去掉就好
def sen_email():
    msg_from = '825361948@qq.com'  # 发送方邮箱
    passwd = 'kcmiynybahsfbfej'  # 填入发送方邮箱的授权码（就是刚刚你拿到的那个授权码）
    msg_to = '825361948@qq.com'  # 收件人邮箱

    msg = MIMEMultipart()

    subject = "APItest Test Report Email"  # 主题
    text_content = "Hi，附件为本次接口测试的结果报告"
    text = MIMEText(text_content)
    msg.attach(text)

    # docFile = '/Users/wenjiehe/PycharmProjects/untitled6/Class01/result-test002.xls'
    # if file_path:  # 最开始的函数参数我默认设置了None ，想添加附件，自行更改一下就好
    # file_path = '/Users/wenjiehe/PycharmProjects/untitled6/Class01/result-test002.xls'
    docFile = '/Users/wenjiehe/Documents/GitHub/testapi-hewenjie/APItest/result-jingan2020test.xls'
    docApart = MIMEApplication(open(docFile, 'rb').read())
    docApart.add_header('Content-Disposition', 'attachment', filename=docFile)
    msg.attach(docApart)

    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print
    "发送成功"




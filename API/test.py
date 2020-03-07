# -*- encoding=utf8 -*-
__author__ = "wenjiehe"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

#点击“闵行报”中文
poco(text="闵行报").click()
sleep(1.0)
poco("android.widget.FrameLayout").offspring("com.wdit.shrmtmh:id/rv_pop").child("com.wdit.shrmtmh:id/llyt_item")[0].child("com.wdit.shrmtmh:id/tv_title").click()

poco("com.wdit.shrmtmh:id/iv_click_back").click()
#点击“闵行报”英文
poco("android.widget.FrameLayout").offspring("com.wdit.shrmtmh:id/rv_pop").child("com.wdit.shrmtmh:id/llyt_item")[1].child("com.wdit.shrmtmh:id/iv_icon").click()

poco("com.wdit.shrmtmh:id/iv_click_back").click()
#点击“城事”
poco(text="城事").click()

poco("com.wdit.shrmtmh:id/iv_click_back").click()
#返回
keyevent("BACK")

#点击广播
poco(text="广播").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#点击电视
poco(text="电视").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/btn_click_back").click()
#微距阵
poco(text="微矩阵").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#区长直通车
poco(text="区长直通车").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#闵行大联动
poco(text="闵行大联动").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#在线访谈
poco(text="在线访谈").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_back").click()
sleep(1.0)
#物业直通车
poco(text="物业直通车").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
sleep(1.0)
#邻里中心
poco(text="物业直通车").swipe([-0.7171, -0.0033])
sleep(1.0)
poco(text="邻里中心").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
sleep(1.0)
#行政服务
poco(text="行政服务").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
sleep(1.0)
#闵行公园
poco(text="闵行公园").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
sleep(1.0)
#闵行菜价
poco(text="闵行公园").swipe([-0.6283, -0.0099])
sleep(1.0)
poco(text="闵行菜价").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
sleep(1.0)
#教育资源
poco(text="教育频道").click()
sleep(1.0)
poco(text="服务").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/iv_click_back").click()
sleep(1.0)


#点击社区
poco(text="社区").click()
value = poco("com.wdit.shrmtmh:id/tv_time").attr("text")
assert_equal(value, "2019-08-04", "进入社区成功")
#点击稿件
poco(text="世界教育机器人大赛上海公开赛在宝山开赛").click()
value = poco("com.wdit.shrmtmh:id/et_click_input_comment").attr("text")
try:
    assert_equal(value, "我来说两句...", "进入稿件页成功")
except AssertionError:
    print("进入稿件页失败")
#稿件评论
poco("com.wdit.shrmtmh:id/et_click_input_comment").click()
poco("com.wdit.shrmtmh:id/et_comment").set_text("不错")
poco("com.wdit.shrmtmh:id/et_comment").click()
poco("com.wdit.shrmtmh:id/tv_click_fa_bu").click()
#收藏
poco("com.wdit.shrmtmh:id/btn_click_sc").click()
#稿件微信转发
poco("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="微信").click()
poco(text="Hahn小杰").click()
poco("com.tencent.mm:id/b47").click()
value = poco("com.tencent.mm:id/b4i").attr("text")
try:
    assert_equal(value, "已发送", "微信转发成功")
except AssertionError:
    print("微信转发失败")
poco("com.tencent.mm:id/b46").click()
#稿件QQ转发
poco("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="QQ").click()
poco(text="Klaus、").click()
poco("com.tencent.mobileqq:id/dialogRightBtn").click()
sleep(1.0)
value = poco("com.tencent.mobileqq:id/dialogText").attr("text")
try:
    assert_equal(value, "分享成功", "QQ转发成功")
except AssertionError:
    print("QQ转发失败")
poco("com.tencent.mobileqq:id/dialogLeftBtn").click()
#返回首页
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#视频菜单
poco(text="视频").click()
#打开短视频
poco(text="短视频").click()
value = poco("com.wdit.shrmtmh:id/tv_value1").attr("text")
try:
    assert_equal(value, "高温酷暑 区委书记朱芝松带队慰问一线工作人员", "进入短视频成功")
except AssertionError:
    print("进入短视频失败")
#点击短视频
poco("android.widget.LinearLayout").offspring("com.wdit.shrmtmh:id/viewPager").offspring("com.wdit.shrmtmh:id/emptyRecyclerView").child("android.widget.RelativeLayout")[0].child("com.wdit.shrmtmh:id/iv_video").click()
sleep(1.0)
#点赞
poco("com.wdit.shrmtmh:id/btn_click_like").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_value_like").attr("text")
try:
    assert_equal(value, "16", "点赞成功")
except AssertionError:
    print("点赞失败")
#取消点赞
poco("com.wdit.shrmtmh:id/btn_click_like").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/btn_click_like").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_value_like").attr("text")
try:
    assert_equal(value, "15", "取消点赞成功")
except AssertionError:
    print("取消点赞失败")
#收藏
poco("com.wdit.shrmtmh:id/btn_click_collection").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_value_collection").attr("text")
try:
    assert_equal(value, "1", "收藏成功")
except AssertionError:
    print("收藏失败")
sleep(1.0)
#取消收藏
poco("com.wdit.shrmtmh:id/btn_click_collection").click()
sleep(1.0)
#短视频评论
poco("com.wdit.shrmtmh:id/btn_click_comment").click()
poco("com.wdit.shrmtmh:id/et_comment").click()
poco("com.wdit.shrmtmh:id/et_comment").set_text("不错")
poco("com.wdit.shrmtmh:id/tv_click_fa_bu").click()
#短视频微信转发
poco("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="微信").click()
poco(text="Hahn小杰").click()
poco("com.tencent.mm:id/b47").click()
value = poco("com.tencent.mm:id/b4i").attr("text")
try:
    assert_equal(value, "已发送", "微信转发成功")
except AssertionError:
    print("微信转发失败")
poco("com.tencent.mm:id/b46").click()
#短视频QQ分享
poco("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="QQ").click()
poco(text="Klaus、").click()
poco("com.tencent.mobileqq:id/dialogRightBtn").click()
sleep(1.0)
value = poco("com.tencent.mobileqq:id/dialogText").attr("text")
try:
    assert_equal(value, "分享成功", "QQ转发成功")
except AssertionError:
    print("QQ转发失败")
poco("com.tencent.mobileqq:id/dialogLeftBtn").click()
#举报
poco("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="举报").click()
value = poco("com.wdit.shrmtmh:id/tv_value").attr("text")
try:
    assert_equal(value, "标题夸张", "打开举报选项成功")
except AssertionError:
    print("打开举报选项失败")
poco(text="旧闻重复").click()
#关闭短视频
poco("com.wdit.shrmtmh:id/iv_click_back").click()
value = poco("com.wdit.shrmtmh:id/tv_value1").attr("text")
try:
    assert_equal(value, "高温酷暑 区委书记朱芝松带队慰问一线工作人员", "关闭短视频成功")
except AssertionError:
    print("关闭短视频失败")
#进入闵行视频列表
poco(text="闵行新闻").click()
#列表点赞
poco("android.widget.LinearLayout").offspring("com.wdit.shrmtmh:id/viewPager").offspring("com.wdit.shrmtmh:id/llyt_add_view").offspring("com.wdit.shrmtmh:id/emptyRecyclerView").child("android.widget.LinearLayout")[0].child("android.widget.FrameLayout")[1].offspring("com.wdit.shrmtmh:id/btn_click_like").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_like_count").attr("text")
try:
    assert_equal(value, "1", "视频列表点赞成功")
except AssertionError:
    print("视频列表点赞失败")
#列表取消点赞
poco("android.widget.LinearLayout").offspring("com.wdit.shrmtmh:id/viewPager").offspring("com.wdit.shrmtmh:id/llyt_add_view").offspring("com.wdit.shrmtmh:id/emptyRecyclerView").child("android.widget.LinearLayout")[0].child("android.widget.FrameLayout")[1].offspring("com.wdit.shrmtmh:id/btn_click_like").click()
sleep(1.0)
#列表播放

sleep(1.0)
#列表微信转发
poco("com.wdit.shrmtmh:id/btn_click_share").click()
sleep(1.0)
poco(text="微信").click()
poco(text="Hahn小杰").click()
poco("com.tencent.mm:id/b47").click()
value = poco("com.tencent.mm:id/b4i").attr("text")
try:
    assert_equal(value, "已发送", "微信转发成功")
except AssertionError:
    print("微信转发失败")
poco("com.tencent.mm:id/b46").click()
#列表QQ转发
poco("android.widget.LinearLayout").offspring("com.wdit.shrmtmh:id/viewPager").offspring("com.wdit.shrmtmh:id/llyt_add_view").offspring("com.wdit.shrmtmh:id/emptyRecyclerView").child("android.widget.LinearLayout")[0].child("android.widget.FrameLayout")[1].offspring("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="QQ").click()
poco(text="Klaus、").click()
poco("com.tencent.mobileqq:id/dialogRightBtn").click()
sleep(1.0)
value = poco("com.tencent.mobileqq:id/dialogText").attr("text")
try:
    assert_equal(value, "分享成功", "QQ转发成功")
except AssertionError:
    print("QQ转发失败")
poco("com.tencent.mobileqq:id/dialogLeftBtn").click()
#列表举报
poco("android.widget.LinearLayout").offspring("com.wdit.shrmtmh:id/viewPager").offspring("com.wdit.shrmtmh:id/llyt_add_view").offspring("com.wdit.shrmtmh:id/emptyRecyclerView").child("android.widget.LinearLayout")[0].child("android.widget.FrameLayout")[1].offspring("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="举报").click()
value = poco("com.wdit.shrmtmh:id/tv_value").attr("text")
try:
    assert_equal(value, "标题夸张", "打开举报选项成功")
except AssertionError:
    print("打开举报选项失败")
poco(text="错别字多").click()
#进入原生视频详情页
poco("android.widget.LinearLayout").offspring("com.wdit.shrmtmh:id/viewPager").offspring("com.wdit.shrmtmh:id/llyt_add_view").offspring("com.wdit.shrmtmh:id/emptyRecyclerView").child("android.widget.LinearLayout")[0].child("com.wdit.shrmtmh:id/tv_title").click()
#视频点赞
poco("com.wdit.shrmtmh:id/tv_value_like").click()
value = poco("com.wdit.shrmtmh:id/tv_value_like").attr("text")
try:
    assert_equal(value, "1", "视频详情页点赞成功")
except AssertionError:
    print("视频详情页点赞失败")
#视频详情页取消点赞
poco("com.wdit.shrmtmh:id/tv_value_like").click()
sleep(1.0)
#收藏
poco("com.wdit.shrmtmh:id/tv_value_collection").click()
sleep(1.0)
poco("com.wdit.shrmtmh:id/tv_value_collection").click()
sleep(1.0)
#评论点赞
poco("com.wdit.shrmtmh:id/tv_click_like").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_click_like").attr("text")
try:
    assert_equal(value, "1", "视频评论点赞成功")
except AssertionError:
    print("视频评论点赞失败")
sleep(1.0)
poco("com.wdit.shrmtmh:id/tv_click_like").click()
sleep(1.0)
#评论
poco("com.wdit.shrmtmh:id/et_click_input_comment").click()
poco("com.wdit.shrmtmh:id/et_click_input_comment").set_text("不错")
poco("com.wdit.shrmtmh:id/tv_click_publish").click()
#微信分享
poco("com.wdit.shrmtmh:id/tv_value_share").click()
poco(text="微信").click()
poco(text="Hahn小杰").click()
poco("com.tencent.mm:id/b47").click()
value = poco("com.tencent.mm:id/b4i").attr("text")
try:
    assert_equal(value, "已发送", "微信转发成功")
except AssertionError:
    print("微信转发失败")
poco("com.tencent.mm:id/b46").click()
#微信分享2
poco("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="微信").click()
poco(text="Hahn小杰").click()
poco("com.tencent.mm:id/b47").click()
value = poco("com.tencent.mm:id/b4i").attr("text")
try:
    assert_equal(value, "已发送", "微信转发成功")
except AssertionError:
    print("微信转发失败")
poco("com.tencent.mm:id/b46").click()
#QQ分享1
poco("com.wdit.shrmtmh:id/tv_value_share").click()
poco(text="QQ").click()
poco(text="Klaus、").click()
poco("com.tencent.mobileqq:id/dialogRightBtn").click()
sleep(1.0)

value = poco("com.tencent.mobileqq:id/dialogText").attr("text")
try:
    assert_equal(value, "分享成功", "QQ转发成功")
except AssertionError:
    print("QQ转发失败")
poco("com.tencent.mobileqq:id/dialogLeftBtn").click()
#QQ分享2
poco("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="QQ").click()
poco(text="Klaus、").click()
poco("com.tencent.mobileqq:id/dialogRightBtn").click()
sleep(1.0)

value = poco("com.tencent.mobileqq:id/dialogText").attr("text")
try:
    assert_equal(value, "分享成功", "QQ转发成功")
except AssertionError:
    print("QQ转发失败")
poco("com.tencent.mobileqq:id/dialogLeftBtn").click()
#举报
poco("com.wdit.shrmtmh:id/tv_value_share").click()
poco(text="举报").click()
poco(text="广告软文").click()
poco("com.wdit.shrmtmh:id/btn_click_share").click()
poco(text="举报").click()
poco(text="旧闻重复").click()
#返回视频
poco("com.wdit.shrmtmh:id/btn_click_back").click()
#我的
poco("android.widget.LinearLayout").offspring("com.wdit.shrmtmh:id/bottomMenutTab").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[4].offspring("com.wdit.shrmtmh:id/iv_tab_icon").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_user_desp").attr("text")
try:
    assert_equal(value, "闵行怡动", "进入我的成功")
except AssertionError:
    print("进入我的失败")
#积分
poco(text="积分").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "我的积分", "进入积分成功")
except AssertionError:
    print("进入积分失败")
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#收藏
poco(text="收藏").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "我的收藏", "进入收藏成功")
except AssertionError:
    print("进入收藏失败")
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#消息
poco(text="消息").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "消息中心", "进入消息成功")
except AssertionError:
    print("进入消息失败")
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#我的足迹
poco(text="我的足迹").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "我的足迹", "进入我的足迹成功")
except AssertionError:
    print("进入我的足迹失败")
#清空足迹并返回
poco("com.wdit.shrmtmh:id/tv_click_right").click()
poco("com.wdit.shrmtmh:id/tv_click_confirm").click()
value = poco("com.wdit.shrmtmh:id/tv_value_hint").attr("text")
try:
    assert_equal(value, "暂无数据", "清空浏览数据成功")
except AssertionError:
    print("清空浏览数据失败")
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#我的评论
poco(text="我的评论").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "我的评论", "进入我的评论成功")
except AssertionError:
    print("进入我的评论失败")
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#我要爆料
poco(text="我要爆料").click()
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "我要爆料", "进入我要爆料成功")
except AssertionError:
    print("进入我要爆料失败")
poco("com.wdit.shrmtmh:id/et_content").set_text("不错")
poco("com.wdit.shrmtmh:id/tv_click_submit").click()
value = poco("com.wdit.shrmtmh:id/tv_user_desp").attr("text")
try:
    assert_equal(value, "闵行怡动", "爆料成功")
except AssertionError:
    print("爆料失败")
#邀请码
poco("com.wdit.shrmtmh:id/tv_invite_title_code").click()
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "我的邀请码", "进入我的邀请码成功")
except AssertionError:
    print("进入我的邀请码失败")
poco("com.wdit.shrmtmh:id/view_click_save").click()
#头像
poco("com.wdit.shrmtmh:id/iv_user_logo").click()
sleep(1.0)
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "个人资料", "进入个人资料成功")
except AssertionError:
    print("进入个人资料失败")
#修改昵称
poco("com.wdit.shrmtmh:id/et_user_name").set_text("Hahn666")
#修改性别
poco("com.wdit.shrmtmh:id/rb_user_female").click()
#修改生日
poco("com.wdit.shrmtmh:id/tv_user_birthday").click()
poco(text="02").click()
poco("android:id/button1").click()
#修改头像
poco("com.wdit.shrmtmh:id/iv_user_picture").click()
poco(text="相册").click()
poco("smartisanos:id/contentPanel").offspring("smartisanos:id/gridView").child("android.widget.RelativeLayout")[2].child("smartisanos:id/icon_image").click()
poco("拍摄时间： null").click()
poco("完成").click()
poco("com.wdit.shrmtmh:id/tv_click_save").click()
value = poco("com.wdit.shrmtmh:id/tv_user_desp").attr("text")
try:
    assert_equal(value, "闵行怡动", "修改个人资料成功")
except AssertionError:
    print("修改个人资料失败")
#系统设置
poco(text="系统设置").click()
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "系统设置", "进入系统设置成功")
except AssertionError:
    print("进入系统设置失败")
#获取版本号
poco(text="版本号").click()
#清缓存
poco("com.wdit.shrmtmh:id/tv_clear_cache").click()
#用户协议
poco(text="用户协议").click()
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "用户协议", "进入用户协议成功")
except AssertionError:
    print("进入用户协议失败")
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#隐私协议
poco(text="隐私协议").click()
value = poco("com.wdit.shrmtmh:id/tv_title").attr("text")
try:
    assert_equal(value, "隐私协议", "进入隐私协议成功")
except AssertionError:
    print("进入隐私协议失败")
poco("com.wdit.shrmtmh:id/iv_click_back").click()
#返回
poco("com.wdit.shrmtmh:id/iv_click_back").click()















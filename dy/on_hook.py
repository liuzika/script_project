from yyds import *
from dy.utils import control_click, set_text_, odds


def main(task_id, task_params) -> TaskRet:
    pkg = "com.ss.android.ugc.aweme"
    params = task_params
    # params = {
    #     "duration": 60,  # 养号时长，分钟
    #     "user_info": {"is": True, "odds": 20},  # 随机查看用户
    #     "star": {"is": True, "odds": 20},  # 是否随机点赞视频
    #     "comment": {"is": True, "odds": 20, "text": "评论内容"},  # 是否随机评论
    #     "concern": {"is": True, "odds": 10},  # 是否随机关注用户
    #     "browse_comments": {"is": True, "odds": 10, "is_star": True, "star_odds": 20},  # 是否随机浏览评论区
    # }
    home_activity = ".splash.SplashActivity"
    engine_set_debug(True)
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(5)
    duration, user_info, star, comment, concern, browse_comments = params.get("duration"), params.get(
        "user_info"), params.get("star"), params.get("comment"), params.get("concern"), params.get("browse_comments")
    stop_time = time.time() + duration * 60
    try:
        DeviceScreen.init()  # 初始化设备参数
        while time.time() <= stop_time:
            if home_activity == device_foreground().activity_name:
                swipe_up()
                sleep(random.randint(3, 10))  # 视频停留时间
                # 随机点进用户里面去查看
                if user_info["is"] and odds(user_info["odds"]):
                    control_click(5, resource_id="com.ss.android.ugc.aweme:id/title", index="0")  # 用户界面
                    if ui_exist(resource_id="com.ss.android.ugc.aweme:id/7a"):
                        control_click(class_="android.widget.ImageView",  index="2")  # 用户界面
                    swipe_up()
                    sleep(2)
                    control_click(resource_id="com.ss.android.ugc.aweme:id/back_btn", content_desc="返回")
                # 随机点赞
                if star["is"] and odds(star["odds"]):
                    control_click(resource_id="com.ss.android.ugc.aweme:id/ei0")  # 点击爱心点赞
                # 随机评论
                if comment["is"] and odds(comment["odds"]):
                    control_click(resource_id="com.ss.android.ugc.aweme:id/czq")  # 打开评论区
                    control_click(resource_id="com.ss.android.ugc.aweme:id/cyh")  # 聚焦输入框
                    set_text_(comment["text"])  # 粘贴评论内容
                    control_click(resource_id="com.ss.android.ugc.aweme:id/c1s", text="发送")  # 发送评论
                    control_click(resource_id="com.ss.android.ugc.aweme:id/back_btn", content_desc="关闭")  # 关闭评论区
                # 随机关注用户
                if concern["is"] and odds(concern["odds"]):
                    control_click(resource_id="com.ss.android.ugc.aweme:id/g+h")  # 点击加号关注
                # 随机浏览评论区,点赞评论
                if browse_comments["is"] and odds(browse_comments["odds"]):
                    control_click(resource_id="com.ss.android.ugc.aweme:id/czq")  # 打开评论区
                    control_click(resource_id="com.ss.android.ugc.aweme:id/hkj", content_desc="放大评论区")  # 放大评论区
                    count = random.randint(1, 10)  # 评论区浏览次数，滑动次数
                    for i in range(count):
                        # 随机评论区点赞
                        if browse_comments["is_star"] and odds(browse_comments["star_odds"]):
                            star_list = ui_match(resource_id="com.ss.android.ugc.aweme:id/ei+",
                                                 content_desc="赞.*未选中")
                            for item in star_list:
                                if odds(50):
                                    control_click(node=item)
                        swipe_up()
                        sleep(2)
                    control_click(resource_id="com.ss.android.ugc.aweme:id/back_btn", content_desc="关闭")  # 关闭评论区
            else:
                open_app(pkg)
        return TaskRet(task_id, True, "养号结束")
    except Exception as e:
        log_d(e)
        return TaskRet(task_id, False, "异常中断")

from yyds import *
from utils import control_click, set_text_, odds, try_func


@try_func
def main(task, pkg) -> bool:
    home_activity = ".splash.SplashActivity"
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(5)
    duration, user_info, star, comment, concern, browse_comments = task.params.get("duration"), task.params.get(
        "user_info"), task.params.get("star"), task.params.get("comment"), task.params.get("concern"), task.params.get(
        "browse_comments")
    stop_time = time.time() + duration * 60
    DeviceScreen.init()  # 初始化设备参数
    while time.time() <= stop_time:
        if home_activity == device_foreground().activity_name:
            swipe_up()
            sleep(random.randint(3, 10))  # 视频停留时间
            # 随机点进用户里面去查看
            if user_info["is"] and odds(user_info["odds"]):
                control_click(5, resource_id="com.ss.android.ugc.aweme:id/title", index="0")  # 用户界面
                if ui_exist(resource_id="com.ss.android.ugc.aweme:id/7a"):
                    control_click(class_="android.widget.ImageView", index="2")
                elif ui_exist(resource_id="com.ss.android.ugc.aweme:id/e4-"):
                    key_back()
                swipe_up()
                sleep(2)
                control_click(resource_id="com.ss.android.ugc.aweme:id/back_btn", content_desc="返回")
                if ui_exist(resource_id="com.ss.android.ugc.aweme:id/iv_back"):
                    control_click(resource_id="com.ss.android.ugc.aweme:id/iv_back")
                    control_click(resource_id="com.ss.android.ugc.aweme:id/goh", text="直接退出")
            # 随机点赞
            if star["is"] and odds(star["odds"]):
                control_click(resource_id="com.ss.android.ugc.aweme:id/ei0")  # 点击爱心点赞
            # 随机评论
            if comment["is"] and odds(comment["odds"]):
                if ui_exist(resource_id="com.ss.android.ugc.aweme:id/czq", content_desc="评论评论，按钮"):
                    control_click(resource_id="com.ss.android.ugc.aweme:id/czq")  # 打开评论区
                else:
                    control_click(resource_id="com.ss.android.ugc.aweme:id/czq")  # 打开评论区
                    control_click(resource_id="com.ss.android.ugc.aweme:id/cyh")  # 聚焦输入框
                set_text_(comment["text"])  # 粘贴评论内容
                control_click(8, resource_id="com.ss.android.ugc.aweme:id/c1s", text="发送")  # 发送评论
                control_click(resource_id="com.ss.android.ugc.aweme:id/back_btn", content_desc="关闭")  # 关闭评论区
            # 随机关注用户
            if concern["is"] and odds(concern["odds"]):
                control_click(resource_id="com.ss.android.ugc.aweme:id/g+h")  # 点击加号关注
            # 随机浏览评论区,点赞评论
            if browse_comments["is"] and odds(
                    browse_comments["odds"] and not ui_exist(resource_id="com.ss.android.ugc.aweme:id/czq",
                                                             content_desc="评论评论，按钮")):
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
            stop_app(pkg)
            sleep(2)
            open_app(pkg)
    task.update_task_status(TaskStatus.DEVICE_FINISH, "养号执行完成")
    return True

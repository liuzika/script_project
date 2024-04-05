from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    task_params = task.params
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    start_app(pkg)
    duration, user_info, star, comment, concern, browse, stat_comment, comment_odds = task_params.get(
        "duration"), task_params.get(
        "user_info"), task_params.get("star"), task_params.get("comment"), task_params.get("concern"), task_params.get(
        "browse"), task_params.get("stat_comment"), task_params.get("comment_odds")
    stop_time = time.time() + duration * 60
    while time.time() <= stop_time:
        if home_activity == device_foreground().activity_name:
            swipe_up()
            sleep(random.randint(3, 10))  # 视频停留时间
            # 随机点进用户里面去查看
            if user_info and odds(int(user_info)):
                click_ui_find_one(5, resource_id="com.zhiliaoapp.musically:id/title", index="0")  # 用户界面
                # if ui_exist(resource_id="com.ss.android.ugc.aweme:id/7a"):
                #     control_click(class_="android.widget.ImageView", index="2")
                # elif ui_exist(resource_id="com.ss.android.ugc.aweme:id/e4-"):
                #     key_back()
                swipe_up()
                sleep(2)
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/hp1")
                # if ui_exist(resource_id="com.ss.android.ugc.aweme:id/iv_back"):
                #     control_click(resource_id="com.ss.android.ugc.aweme:id/iv_back")
                #     control_click(resource_id="com.ss.android.ugc.aweme:id/goh", text="直接退出")
            # 随机点赞
            if star and odds(int(star)):
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/cnv", content_desc="Like")  # 点击爱心点赞
            # 随机评论
            if comment_odds and odds(int(comment_odds)):
                # if ui_exist(resource_id="com.zhiliaoapp.musically:id/buv", content_desc="评论评论，按钮"):
                #     control_click(resource_id="com.zhiliaoapp.musically:id/buv")  # 打开评论区
                # else:
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/buv")  # 打开评论区
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/bui")  # 聚焦输入框
                set_text_(comment)  # 粘贴评论内容
                click_ui_find_one(8, resource_id="com.zhiliaoapp.musically:id/bwe", content_desc="Post comment")  # 发送评论
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/aio", content_desc="Close comments")  # 关闭评论区
            # 随机关注用户
            if concern and odds(int(concern)):
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/e1n")  # 点击加号关注
            # 随机浏览评论区,点赞评论
            if browse and odds(int(browse)):
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/buv")  # 打开评论区
                # control_click(resource_id="com.ss.android.ugc.aweme:id/hkj", content_desc="放大评论区")  # 放大评论区
                count = random.randint(1, 10)  # 评论区浏览次数，滑动次数
                for i in range(count):
                    # 随机评论区点赞
                    if stat_comment and odds(int(stat_comment)):
                        star_list = ui_match(resource_id="com.zhiliaoapp.musically:id/fp7",
                                             content_desc="Like or undo like")
                        for item in star_list:
                            if odds(50):
                                click_ui_find_one(node=item)
                    swipe_up()
                    sleep(2)
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/aio", content_desc="Close comments")  # 关闭评论区
        else:
            stop_app(pkg)
            sleep(2)
            open_app(pkg)
    task.update_task_status(TaskStatus.DEVICE_FINISH, "养号结束")
    return True

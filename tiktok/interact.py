from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    NotificationDetailActivity = ".socialnotice.view.activity.NotificationDetailActivity"
    start_app(pkg)
    if device_foreground().activity_name == home_activity:
        click_ui_find_one(resource_id="com.ss.android.ugc.aweme:id/b7p")
        click_ui_find_one(content_desc="消息，按钮", resource_id="com.ss.android.ugc.aweme:id/vhl")
        hdxx = ui_match(resource_id="com.ss.android.ugc.aweme:id/red_tips_count_view")
        if len(hdxx):
            click_ui_find_one(6, node=hdxx[0])
            if device_foreground().activity_name == NotificationDetailActivity:
                count: int = int(hdxx[0].text)
                completed_count: int = 0
                replied_list: list = []
                swipe_max_count = 10
                swipe_count = 0
                while count > completed_count:
                    hot_list = ui_match(resource_id="com.ss.android.ugc.aweme:id/ox_")
                    comment_list = [i for item in hot_list for i in ui_sib(item) if
                                    i.id == "com.ss.android.ugc.aweme:id/c1="]
                    for node in comment_list:
                        click_ui_find_one(5, node=node)
                        set_text_("回复内容")
                        click_ui_find_one(text="发送", resource_id="com.ss.android.ugc.aweme:id/c1s")
                        completed_count += 1
                        replied_list.append(node)
                        if completed_count >= count:
                            break
                    if ui_exist(text="暂时没有更多了") or swipe_max_count == swipe_count:
                        break
                    swipe_up()
                    sleep(1)
                    swipe_max_count += 1
                click_ui_find_one(content_desc="返回.*", resource_id="com.ss.android.ugc.aweme:id/iv_back")
            else:
                click_ui_find_one(content_desc="返回", resource_id="com.ss.android.ugc.aweme:id/back_btn")
        while ui_exist(resource_id="com.ss.android.ugc.aweme:id/trn"):
            private_letter_list = ui_match(resource_id="com.ss.android.ugc.aweme:id/rx6")
            for node in private_letter_list:
                click_ui_find_one(5, node=node)
                click_ui_find_one(hind_text="发送消息", resource_id="com.ss.android.ugc.aweme:id/n=m")
                set_text_("回复内容")
                click_ui_find_one(5, content_desc="发送", resource_id="com.ss.android.ugc.aweme:id/jjm")
                click_ui_find_one(content_desc="返回.*", resource_id="com.ss.android.ugc.aweme:id/lqj")
            if ui_exist(text="暂时没有更多了"):
                break
            click_ui_find_one(text="查看全部")
            swipe_up()
        task.update_task_status(TaskStatus.DEVICE_FINISH, "互动与私聊执行完成")
        return True
    return False

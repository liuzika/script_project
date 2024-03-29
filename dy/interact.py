from yyds import *
from dy.utils import control_click, set_text_


def main(task_id) -> TaskRet:
    try:
        pkg = "com.ss.android.ugc.aweme"
        home_activity = ".splash.SplashActivity"
        NotificationDetailActivity = ".socialnotice.view.activity.NotificationDetailActivity"
        engine_set_debug(True)
        stop_app(pkg)
        sleep(2)
        open_app(pkg)
        sleep(5)
        DeviceScreen.init()
        if device_foreground().activity_name == home_activity:
            control_click(limit=1, resource_id="com.ss.android.ugc.aweme:id/b7p")
            control_click(limit=1, content_desc="消息，按钮", resource_id="com.ss.android.ugc.aweme:id/vhl")
            hdxx = ui_match(limit=1, resource_id="com.ss.android.ugc.aweme:id/red_tips_count_view")
            if len(hdxx):
                control_click(6, node=hdxx[0])
                if device_foreground().activity_name == NotificationDetailActivity:
                    count: int = int(hdxx[0].text)
                    completed_count: int = 0
                    replied_list: list = []
                    swipe_max_count = 10
                    swipe_count = 0
                    while count > completed_count:
                        hot_list = ui_match(resource_id="com.ss.android.ugc.aweme:id/ox_")
                        comment_list = [i for item in hot_list for i in ui_sib(item) if i.id == "com.ss.android.ugc.aweme:id/c1="]
                        for node in comment_list:
                            control_click(5, node=node)
                            set_text_("回复内容")
                            control_click(limit=1, text="发送", resource_id="com.ss.android.ugc.aweme:id/c1s")
                            completed_count += 1
                            replied_list.append(node)
                            if completed_count >= count:
                                break
                        if ui_exist(text="暂时没有更多了") or swipe_max_count == swipe_count:
                            break
                        swipe_up()
                        sleep(1)
                        swipe_max_count += 1
                    control_click(limit=1, content_desc="返回.*", resource_id="com.ss.android.ugc.aweme:id/iv_back")
                else:
                    control_click(limit=1, content_desc="返回", resource_id="com.ss.android.ugc.aweme:id/back_btn")
            while ui_exist(resource_id="com.ss.android.ugc.aweme:id/trn"):
                private_letter_list = ui_match(resource_id="com.ss.android.ugc.aweme:id/rx6")
                for node in private_letter_list:
                    control_click(5, node=node)
                    control_click(limit=1, hind_text="发送消息", resource_id="com.ss.android.ugc.aweme:id/n=m")
                    set_text_("回复内容")
                    control_click(5, limit=1, content_desc="发送", resource_id="com.ss.android.ugc.aweme:id/jjm")
                    control_click(limit=1, content_desc="返回.*", resource_id="com.ss.android.ugc.aweme:id/lqj")
                if ui_exist(text="暂时没有更多了"):
                    break
                control_click(limit=1, text="查看全部")
                swipe_up()
            return TaskRet(task_id, True, "私聊互动结束")
    except Exception as e:
        log_d(e)
        return TaskRet(task_id, False, "脚本异常中断")

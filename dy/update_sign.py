from yyds import *
from dy.utils import set_text_, control_click


def main(task):
    pkg = "com.ss.android.ugc.aweme"
    home_activity = ".splash.SplashActivity"
    profile_activity = ".profile.ui.ProfileEditActivity"
    engine_set_debug(True)
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(5)
    try:
        if device_foreground().activity_name == home_activity:
            control_click(limit=1, content_desc="我，按钮", resource_id="com.ss.android.ugc.aweme:id/vhl")
            control_click(limit=1, resource_id="com.ss.android.ugc.aweme:id/ory")
            if device_foreground().activity_name == profile_activity:
                control_click(limit=1, hind_text="介绍喜好、个性或@你的亲友",
                              resource_id="com.ss.android.ugc.aweme:id/tv_profile_item_content")
                control_click(limit=1, hind_text="介绍喜好、个性或@你的亲友", resource_id="com.ss.android.ugc.aweme:id/f7n")
                set_text_(task.params.sign)
                control_click(5, limit=1, text="保存", resource_id="com.ss.android.ugc.aweme:id/right_btn")
                stop_app(pkg)
                task.update_task_status(TaskStatus.DEVICE_FINISH, '成功修改简介')
    except Exception as e:
        task.update_task_status(TaskStatus.DEVICE_EXE_ERROR, f"执行错误: {repr(e)}")
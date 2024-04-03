from yyds import *
from dy.utils import set_text_, control_click


def main(task):
    pkg = "com.zhiliaoapp.musically"
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    profile_activity = "com.ss.android.ugc.aweme.profile.ui.ProfileEditActivity"
    nickname = task.params.sign
    engine_set_debug(True)
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(3)
    try:
        if device_foreground().activity_name == home_activity:
            control_click(limit=1, content_desc="Profile", resource_id="com.zhiliaoapp.musically:id/h3j")
            control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/ccu", text="Edit profile")
            if device_foreground().activity_name == profile_activity:
                control_click(limit=1, text="Bio", resource_id="com.zhiliaoapp.musically:id/mht")
                control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/deg")
                set_text_(nickname)
                control_click(10, limit=1, resource_id="com.zhiliaoapp.musically:id/hot")
                stop_app(pkg)
                task.update_task_status(TaskStatus.DEVICE_FINISH, "成功修改昵称")
    except Exception as e:
        task.update_task_status(TaskStatus.DEVICE_EXE_ERROR, f"执行错误: {repr(e)}")

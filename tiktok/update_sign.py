from yyds import *
from dy.utils import set_text_, control_click


def main(task_id, task_params) -> TaskRet:
    pkg = "com.zhiliaoapp.musically"
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    profile_activity = "com.ss.android.ugc.aweme.profile.ui.ProfileEditActivity"
    nickname = task_params.sign
    engine_set_debug(True)
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(3)
    if device_foreground().activity_name == home_activity:
        control_click(limit=1, content_desc="Profile", resource_id="com.zhiliaoapp.musically:id/h3j")
        control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/ccu", text="Edit profile")
        if device_foreground().activity_name == profile_activity:
            control_click(limit=1, text="Bio", resource_id="com.zhiliaoapp.musically:id/mht")
            control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/deg")
            set_text_(nickname)
            control_click(10, limit=1, resource_id="com.zhiliaoapp.musically:id/hot")
            stop_app(pkg)
            return TaskRet(task_id, True, "成功修改昵称")
    return TaskRet(task_id, False, "代码错误")

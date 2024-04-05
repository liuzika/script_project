from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    profile_activity = "com.ss.android.ugc.aweme.profile.ui.ProfileEditActivity"
    nickname = task.params.nickname
    start_app(pkg)
    if device_foreground().activity_name == home_activity:
        control_click(limit=1, content_desc="Profile", resource_id="com.zhiliaoapp.musically:id/h3j")
        control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/ccu", text="Edit profile")
        if device_foreground().activity_name == profile_activity:
            control_click(limit=1, text="Name",
                          resource_id="com.zhiliaoapp.musically:id/mht")
            control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/deg")
            set_text_(nickname)
            control_click(10, limit=1, resource_id="com.zhiliaoapp.musically:id/hot")
            stop_app(pkg)
            task.update_task_status(TaskStatus.DEVICE_FINISH, "成功修改昵称")
            return True
    return False

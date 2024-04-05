from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    profile_activity = "com.ss.android.ugc.aweme.profile.ui.ProfileEditActivity"
    nickname = task.params.sign
    start_app(pkg)
    if device_foreground().activity_name == home_activity:
        click_ui_find_one(content_desc="Profile", resource_id="com.zhiliaoapp.musically:id/h3j")
        click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/ccu", text="Edit profile")
        if device_foreground().activity_name == profile_activity:
            click_ui_find_one(text="Bio", resource_id="com.zhiliaoapp.musically:id/mht")
            click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/deg")
            set_text_(nickname)
            click_ui_find_one(10, resource_id="com.zhiliaoapp.musically:id/hot")
            stop_app(pkg)
            task.update_task_status(TaskStatus.DEVICE_FINISH, "成功修改昵称")
            return True
    return False

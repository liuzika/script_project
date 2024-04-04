from yyds import *
from utils import set_text_, control_click, try_func


@try_func
def main(task, pkg) -> bool:
    home_activity = ".splash.SplashActivity"
    profile_activity = ".profile.ui.ProfileEditActivity"
    TextEditingActivity = "com.ss.android.ugc.gamora.editor.text.TextEditingActivity"
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(5)
    if device_foreground().activity_name == home_activity:
        control_click(limit=1, content_desc="我，按钮", resource_id="com.ss.android.ugc.aweme:id/vhl")
        control_click(limit=1, resource_id="com.ss.android.ugc.aweme:id/ory")
        if device_foreground().activity_name == profile_activity:
            control_click(limit=1, hind_text="介绍喜好、个性或@你的亲友",
                          resource_id="com.ss.android.ugc.aweme:id/tv_profile_item_content")
            control_click(limit=1, hind_text="介绍喜好、个性或@你的亲友", resource_id="com.ss.android.ugc.aweme:id/f7n")
            set_text_(task.params.sign)
            control_click(5, limit=1, text="保存", resource_id="com.ss.android.ugc.aweme:id/right_btn")
            if device_foreground().activity_name == TextEditingActivity:
                control_click(limit=1, content_desc="返回")
                control_click(limit=1, content_desc="清空内容")
            if ui_exist(text=task.params.sign):
                task.update_task_status(TaskStatus.DEVICE_FINISH, '成功修改简介')
                return True
    return False

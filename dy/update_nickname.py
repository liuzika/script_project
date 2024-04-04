from yyds import *
from utils import set_text_, control_click, try_func


@try_func
def main(task, pkg):
    home_activity = ".splash.SplashActivity"
    profile_activity = ".profile.ui.ProfileEditActivity"
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(3)
    if device_foreground().activity_name == home_activity:
        control_click(limit=1, content_desc="我，按钮", resource_id="com.ss.android.ugc.aweme:id/vhl")
        control_click(limit=1, resource_id="com.ss.android.ugc.aweme:id/ory")
        if device_foreground().activity_name == profile_activity:
            control_click(limit=1, hind_text="定制你的专属称呼",
                          resource_id="com.ss.android.ugc.aweme:id/tv_profile_item_content")
            control_click(limit=1, hind_text="记得填写名字哦", resource_id="com.ss.android.ugc.aweme:id/f6-")
            set_text_(task.params.nickname)
            control_click(5, limit=1, text="保存", resource_id="com.ss.android.ugc.aweme:id/right_btn")
            if ui_exist(class_="android.widget.ImageView", text=task.params.nickname):
                task.update_task_status(TaskStatus.DEVICE_FINISH, '成功修改昵称')
            else:
                main(task)
        else:
            pass

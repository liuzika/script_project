from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    home_activity = ".splash.SplashActivity"
    profile_activity = ".profile.ui.ProfileEditActivity"
    TextEditingActivity = "com.ss.android.ugc.gamora.editor.text.TextEditingActivity"
    start_app(pkg)
    if device_foreground().activity_name == home_activity:
        click_ui_find_one(desc="我的按钮", content_desc="我，按钮", resource_id="com.ss.android.ugc.aweme:id/vhl")
        click_ui_find_one(desc="昵称进入个人信息页", resource_id="com.ss.android.ugc.aweme:id/ory")
        if device_foreground().activity_name == profile_activity:
            click_ui_find_one(desc="简介框", hind_text="介绍喜好、个性或@你的亲友",
                              resource_id="com.ss.android.ugc.aweme:id/tv_profile_item_content")
            click_ui_find_one(desc="简介输入框", hind_text="介绍喜好、个性或@你的亲友",
                              resource_id="com.ss.android.ugc.aweme:id/f7n")
            set_text_(task.params.sign)
            click_ui_find_one(5, desc="保存按钮", text="保存", resource_id="com.ss.android.ugc.aweme:id/right_btn")
            if device_foreground().activity_name == TextEditingActivity:
                click_ui_find_one(desc="返回按钮", content_desc="返回")
                click_ui_find_one(desc="清空内容按钮", content_desc="清空内容")
            if ui_exist(text=task.params.sign):
                task.update_task_status(TaskStatus.DEVICE_FINISH, '成功修改简介')
                return True
    return False

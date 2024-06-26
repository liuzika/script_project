from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    home_activity = ".splash.SplashActivity"
    profile_activity = ".profile.ui.ProfileEditActivity"
    start_app(pkg)
    if device_foreground().activity_name == home_activity:
        click_ui_find_one(content_desc="我，按钮", resource_id="com.ss.android.ugc.aweme:id/vhl")
        click_ui_find_one(resource_id="com.ss.android.ugc.aweme:id/ory")
        if device_foreground().activity_name == profile_activity:
            click_ui_find_one(content_desc="更换头像", parent_count="3")
            click_ui_find_one(text="从相册选择", resource_id="com.ss.android.ugc.aweme:id/fg")
            if ui_exist(text="允许", resource_id="com.android.permissioncontroller:id/permission_allow_button"):
                click_ui_find_one(text="允许",
                              resource_id="com.android.permissioncontroller:id/permission_allow_button")
            elif ui_exist(text="去设置", resource_id="com.ss.android.ugc.aweme:id/dw"):
                click_ui_find_one(text="去设置", resource_id="com.ss.android.ugc.aweme:id/dw")
                click_ui_find_one(text="权限", resource_id="android:id/title")
                i = 0
                while i < 3:
                    if ui_exist(text="文件和媒体", resource_id="android:id/title"):
                        click_ui_find_one(text="文件和媒体", resource_id="android:id/title")
                        click_ui_find_one(text="仅允许访问媒体文件",
                                      resource_id="com.android.permissioncontroller:id/allow_foreground_only_radio_button")
                        bring_app_to_top(pkg)
                        sleep(1)
                        break
                    else:
                        swipe(350, 900, 450, 200, 800, is_random=True)
                        i += 1
                    sleep(1)
            find_image_click(task.params.url, min_prob=0.6)
            sleep(2)
            click_ui_find_one(resource_id="com.ss.android.ugc.aweme:id/tv_confirm", text="完成")
            click_ui_find_one(resource_id="com.ss.android.ugc.aweme:id/q+1")
            click_ui_find_one(5, resource_id="com.ss.android.ugc.aweme:id/q+0", text="完成")
            task.update_task_status(TaskStatus.DEVICE_FINISH, "成功修改头像")
            return True
    return False

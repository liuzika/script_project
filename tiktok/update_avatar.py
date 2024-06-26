from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    profile_activity = "com.ss.android.ugc.aweme.profile.ui.ProfileEditActivity"
    start_app(pkg)
    if device_foreground().activity_name == home_activity:
        click_ui_find_one(content_desc="Profile", resource_id="com.zhiliaoapp.musically:id/h3j")
        click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/ccu", text="Edit profile")
        if device_foreground().activity_name == profile_activity:
            click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/f29")
            click_ui_find_one(text="Select from Gallery", resource_id="com.zhiliaoapp.musically:id/pl")
            # if ui_exist(text="允许", resource_id="com.android.permissioncontroller:id/permission_allow_button"):
            #     control_click(text="允许",
            #                   resource_id="com.android.permissioncontroller:id/permission_allow_button")
            # elif ui_exist(text="去设置", resource_id="com.ss.android.ugc.aweme:id/dw"):
            #     control_click(text="去设置", resource_id="com.ss.android.ugc.aweme:id/dw")
            #     control_click(text="权限", resource_id="android:id/title")
            #     i = 0
            #     while i < 3:
            #         if ui_exist(text="文件和媒体", resource_id="android:id/title"):
            #             control_click(text="文件和媒体", resource_id="android:id/title")
            #             control_click(text="仅允许访问媒体文件",
            #                           resource_id="com.android.permissioncontroller:id/allow_foreground_only_radio_button")
            #             bring_app_to_top(pkg)
            #             sleep(1)
            #             break
            #         else:
            #             swipe(350, 900, 450, 200, 800, is_random=True)
            #             i += 1
            #         sleep(1)
            find_image_click(task.params.url, min_prob=0.6)
            sleep(2)
            if ui_exist(text="Image size is too small"):
                task.update_task_status(TaskStatus.DEVICE_EXE_ERROR, "修改头像失败，图片尺寸错误！")
            click_ui_find_one(5, resource_id="com.zhiliaoapp.musically:id/b9m", text="Confirm")
            if device_foreground().activity_name != "com.ss.android.ugc.aweme.profile.ui.CropActivity":
                click_ui_find_one(5, resource_id="com.zhiliaoapp.musically:id/bit")
                if ui_exist(text="Image size is too small"):
                    task.update_task_status(TaskStatus.DEVICE_EXE_ERROR, "修改头像失败，图片尺寸错误！")
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/b9m", text="Confirm")
            if ui_exist(resource_id="com.zhiliaoapp.musically:id/nak", text="Save &amp; post"):
                click_ui_find_one(5, resource_id="com.zhiliaoapp.musically:id/ize",
                              text="Post this photo to Story")
            click_ui_find_one(5, resource_id="com.zhiliaoapp.musically:id/nak", text="Save")
            stop_app(pkg)
            task.update_task_status(TaskStatus.DEVICE_FINISH, "成功修改头像")
            return True
    return False

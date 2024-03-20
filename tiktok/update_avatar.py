from yyds import *
from dy.utils import control_click


def main(task_id, task_params) -> TaskRet:
    pkg = "com.zhiliaoapp.musically"
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    profile_activity = "com.ss.android.ugc.aweme.profile.ui.ProfileEditActivity"
    # avatar_url = task_params.url
    # shell("wget -q -O /sdcard/DCIM/1.jpg " + avatar_url)
    engine_set_debug(True)
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(5)
    if device_foreground().activity_name == home_activity:
        control_click(limit=1, content_desc="Profile", resource_id="com.zhiliaoapp.musically:id/h3j")
        control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/ccu", text="Edit profile")
        if device_foreground().activity_name == profile_activity:
            control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/f29")
            control_click(limit=1, text="Select from Gallery", resource_id="com.zhiliaoapp.musically:id/pl")
            # if ui_exist(text="允许", resource_id="com.android.permissioncontroller:id/permission_allow_button"):
            #     control_click(limit=1, text="允许",
            #                   resource_id="com.android.permissioncontroller:id/permission_allow_button")
            # elif ui_exist(text="去设置", resource_id="com.ss.android.ugc.aweme:id/dw"):
            #     control_click(limit=1, text="去设置", resource_id="com.ss.android.ugc.aweme:id/dw")
            #     control_click(limit=1, text="权限", resource_id="android:id/title")
            #     i = 0
            #     while i < 3:
            #         if ui_exist(text="文件和媒体", resource_id="android:id/title"):
            #             control_click(limit=1, text="文件和媒体", resource_id="android:id/title")
            #             control_click(limit=1, text="仅允许访问媒体文件",
            #                           resource_id="com.android.permissioncontroller:id/allow_foreground_only_radio_button")
            #             bring_app_to_top(pkg)
            #             sleep(1)
            #             break
            #         else:
            #             swipe(350, 900, 450, 200, 800, is_random=True)
            #             i += 1
            #         sleep(1)
            find_image_click(task_params.url, min_prob=0.6)
            sleep(2)
            if ui_exist(text="Image size is too small"):
                return TaskRet(task_id, False, "修改头像失败，图片尺寸错误！")
            control_click(5, limit=1, resource_id="com.zhiliaoapp.musically:id/b9m", text="Confirm")
            if device_foreground().activity_name != "com.ss.android.ugc.aweme.profile.ui.CropActivity":
                control_click(5, limit=1, resource_id="com.zhiliaoapp.musically:id/bit")
                if ui_exist(text="Image size is too small"):
                    return TaskRet(task_id, False, "修改头像失败，图片尺寸错误！")
                control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/b9m", text="Confirm")
            if ui_exist(resource_id="com.zhiliaoapp.musically:id/nak", text="Save &amp; post"):
                control_click(5, limit=1, resource_id="com.zhiliaoapp.musically:id/ize",  text="Post this photo to Story")
            control_click(5, resource_id="com.zhiliaoapp.musically:id/nak", text="Save")
            stop_app(pkg)
            return TaskRet(task_id, True, "成功修改头像")
    return TaskRet(task_id, False, "代码错误")

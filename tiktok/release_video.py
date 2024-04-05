from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    task_params = task.params
    task_params["@user"] = split(task_params['@user'])
    task_params["tag"] = split(task_params['tag'])
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    start_app(pkg)
    if device_foreground().activity_name == home_activity:
        control_click(5, limit=1, content_desc="Create", resource_id="com.zhiliaoapp.musically:id/h3e")
        while device_foreground().activity_name == ".permission.ui.GrantPermissionsActivity":
            control_click(5, limit=1, text="WHILE USING THE APP",
                          resource_id="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        if device_foreground().activity_name == "com.ss.android.ugc.aweme.adaptation.saa.SAAActivity":
            control_click(5, limit=1, resource_id="com.zhiliaoapp.musically:id/b5g")
            control_click(5, limit=1, resource_id="com.zhiliaoapp.musically:id/nwv")
            control_click(limit=1, class_="android.widget.FrameLayout", index="0", focusable="true")
            control_click(limit=1, text="Next")
            if task_params["desc"] or task_params["@user"] or task_params["tag"]:
                control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/d5k")
                text = ""
                if task_params["desc"]:
                    text += task_params["desc"] + " "
                for tag in task_params["tag"]:
                    text += "#" + tag + " "
                set_text_(text)
                sleep(2)
                for user in task_params["@user"]:
                    control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/ac4")
                    control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/kfp")
                    set_yy_input_enable(True)
                    x_input_text(user)
                    sleep(2)
                    control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/bc6", index="0",
                                  class_="android.view.ViewGroup")
            if task_params["address"]:
                control_click(5, limit=1, resource_id="com.zhiliaoapp.musically:id/bfk")
                control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/deg")
                set_text_(task_params["address"])
                sleep(5)
                # if ui_exist(content_desc="没有搜索到相关位置"):
                #     control_click(limit=1, content_desc="返回，按钮")
                # else:
                control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/bms", index="0")
            control_click(limit=1, resource_id="com.zhiliaoapp.musically:id/jfv", content_desc="Post")
            task.update_task_status(TaskStatus.DEVICE_FINISH, "成功发布视频")
            return True
    return False

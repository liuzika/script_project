from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    task_params = task.params
    task_params["@user"] = split(task_params['@user'])
    task_params["tag"] = split(task_params['tag'])
    home_activity = "com.ss.android.ugc.aweme.splash.SplashActivity"
    start_app(pkg)
    if device_foreground().activity_name == home_activity:
        click_ui_find_one(5, content_desc="Create", resource_id="com.zhiliaoapp.musically:id/h3e")
        while device_foreground().activity_name == ".permission.ui.GrantPermissionsActivity":
            click_ui_find_one(5, text="WHILE USING THE APP",
                          resource_id="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        if device_foreground().activity_name == "com.ss.android.ugc.aweme.adaptation.saa.SAAActivity":
            click_ui_find_one(5, resource_id="com.zhiliaoapp.musically:id/b5g")
            click_ui_find_one(5, resource_id="com.zhiliaoapp.musically:id/nwv")
            click_ui_find_one(class_="android.widget.FrameLayout", index="0", focusable="true")
            click_ui_find_one(text="Next")
            if task_params["desc"] or task_params["@user"] or task_params["tag"]:
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/d5k")
                text = ""
                if task_params["desc"]:
                    text += task_params["desc"] + " "
                for tag in task_params["tag"]:
                    text += "#" + tag + " "
                set_text_(text)
                sleep(2)
                for user in task_params["@user"]:
                    click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/ac4")
                    click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/kfp")
                    set_yy_input_enable(True)
                    x_input_text(user)
                    sleep(2)
                    click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/bc6", index="0",
                                  class_="android.view.ViewGroup")
            if task_params["address"]:
                click_ui_find_one(5, resource_id="com.zhiliaoapp.musically:id/bfk")
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/deg")
                set_text_(task_params["address"])
                sleep(5)
                # if ui_exist(content_desc="没有搜索到相关位置"):
                #     control_click(content_desc="返回，按钮")
                # else:
                click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/bms", index="0")
            click_ui_find_one(resource_id="com.zhiliaoapp.musically:id/jfv", content_desc="Post")
            task.update_task_status(TaskStatus.DEVICE_FINISH, "成功发布视频")
            return True
    return False

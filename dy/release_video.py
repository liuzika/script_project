from script_common.utils import *


@try_func
def main(task, pkg) -> bool:
    task_params = task.params
    task_params["@user"] = split(task_params['@user'])
    task_params["tag"] = split(task_params['tag'])
    home_activity = ".splash.SplashActivity"
    GrantPermissionsActivity = ".permission.ui.GrantPermissionsActivity"
    VideoRecordNewActivity = ".shortvideo.ui.VideoRecordNewActivity"
    InfiniEditActivity = ".tools.infini.core.InfiniEditActivity"
    start_app(pkg)
    if device_foreground().activity_name == home_activity:
        click_ui_find_one(resource_id="com.ss.android.ugc.aweme:id/b7p")
        click_ui_find_one(content_desc="拍摄，按钮", resource_id="com.ss.android.ugc.aweme:id/vg+")
        while device_foreground().activity_name == GrantPermissionsActivity:
            click_ui_find_one(5, text="仅在使用该应用时允许",
                              resource_id="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        if device_foreground().activity_name == VideoRecordNewActivity:
            click_ui_find_one(5, resource_id="com.ss.android.ugc.aweme:id/kxq")
            click_ui_find_one(5, resource_id="com.android.permissioncontroller:id/permission_allow_button",
                              text="允许")
            click_ui_find_one(text="视频")
            click_ui_find_one(resource_id="com.ss.android.ugc.aweme:id/root_view", index="0", focusable="true")
            click_ui_find_one(text="下一步")
            if device_foreground().activity_name == InfiniEditActivity:
                click_ui_find_one(5, resource_id="com.ss.android.ugc.aweme:id/orl", text="下一步")
                if task_params["desc"] or task_params["@user"] or task_params["tag"]:
                    click_ui_find_one(resource_id="com.ss.android.ugc.aweme:id/ftr", text="添加作品描述..")
                    text = ""
                    if task_params["desc"]:
                        text += task_params["desc"] + " "
                    for tag in task_params["tag"]:
                        text += "#" + tag + " "
                    set_text_(text)
                    sleep(2)
                    for user in task_params["@user"]:
                        click_ui_find_one(resource_id="com.ss.android.ugc.aweme:id/ac2",
                                          content_desc="@朋友，按钮")
                        set_yy_input_enable(True)
                        x_input_text(user)
                        sleep(2)
                        click_ui_find_one(drawing_order="3", index="0", class_="android.widget.FrameLayout")
                if task_params["address"]:
                    click_ui_find_one(5, resource_id="com.ss.android.ugc.aweme:id/qan")
                    click_ui_find_one(limit=1, class_="com.bytedance.ies.xelement.input.LynxInputView")
                    set_text_("gd")
                    sleep(5)
                    if ui_exist(content_desc="没有搜索到相关位置"):
                        click_ui_find_one(content_desc="返回，按钮")
                    else:
                        click_ui_find_one(class_="com.lynx.tasm.behavior.ui.LynxFlattenUI",
                                          visible_to_user="true",
                                          clickable="true")
                click_ui_find_one(resource_id="com.ss.android.ugc.aweme:id/ran", text="发布")
                task.update_task_status(TaskStatus.DEVICE_FINISH, "成功发布视频")
                return True
    return False

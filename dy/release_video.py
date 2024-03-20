from yyds import *
from dy.utils import control_click, set_text_


def main(task_id, task_params) -> TaskRet:
    pkg = "com.ss.android.ugc.aweme"
    home_activity = ".splash.SplashActivity"
    GrantPermissionsActivity = ".permission.ui.GrantPermissionsActivity"
    VideoRecordNewActivity = ".shortvideo.ui.VideoRecordNewActivity"
    InfiniEditActivity = ".tools.infini.core.InfiniEditActivity"
    engine_set_debug(True)
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(5)
    if device_foreground().activity_name == home_activity:
        control_click(limit=1, resource_id="com.ss.android.ugc.aweme:id/b7p")
        control_click(limit=1, content_desc="拍摄，按钮", resource_id="com.ss.android.ugc.aweme:id/vg+")
        while device_foreground().activity_name == GrantPermissionsActivity:
            control_click(5, limit=1, text="仅在使用该应用时允许",
                          resource_id="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        if device_foreground().activity_name == VideoRecordNewActivity:
            control_click(5, limit=1, resource_id="com.ss.android.ugc.aweme:id/kxq")
            control_click(5, limit=1, resource_id="com.android.permissioncontroller:id/permission_allow_button",
                          text="允许")
            control_click(limit=1, text="视频")
            control_click(limit=1, resource_id="com.ss.android.ugc.aweme:id/root_view", index="0", focusable="true")
            control_click(limit=1, text="下一步")
            if device_foreground().activity_name == InfiniEditActivity:
                control_click(5, limit=1, resource_id="com.ss.android.ugc.aweme:id/orl", text="下一步")
                if task_params["desc"] or task_params["@user"] or task_params["tag"]:
                    control_click(limit=1, resource_id="com.ss.android.ugc.aweme:id/ftr", text="添加作品描述..")
                    text = ""
                    if task_params["desc"]:
                        text += task_params["desc"] + " "
                    for tag in task_params["tag"]:
                        text += "#" + tag + " "
                    set_text_(text)
                    sleep(2)
                    for user in task_params["@user"]:
                        control_click(limit=1, resource_id="com.ss.android.ugc.aweme:id/ac2", content_desc="@朋友，按钮")
                        set_yy_input_enable(True)
                        x_input_text(user)
                        sleep(2)
                        control_click(limit=1, drawing_order="3", index="0", class_="android.widget.FrameLayout")
                if task_params["address"]:
                    control_click(5, limit=1, resource_id="com.ss.android.ugc.aweme:id/qan")
                    control_click(limit=1, class_="com.bytedance.ies.xelement.input.LynxInputView")
                    set_text_("gd")
                    sleep(5)
                    if ui_exist(content_desc="没有搜索到相关位置"):
                        control_click(limit=1, content_desc="返回，按钮")
                    else:
                        control_click(limit=1, class_="com.lynx.tasm.behavior.ui.LynxFlattenUI", visible_to_user="true",
                                      clickable="true")
                control_click(limit=1, resource_id="com.ss.android.ugc.aweme:id/ran", text="发布")
                return TaskRet(task_id, True, "成功发布视频")
    return TaskRet(task_id, False, "代码错误")

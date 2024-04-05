from yyds import *
from script_common.ScriptTask import *
import dy
import tiktok

dy_pkg = "com.ss.android.ugc.aweme"
tiktok_pkg = "com.zhiliaoapp.musically"


class TaskAction(Enum):
    # 修改昵称
    CHANG_NICKNAME = 0
    # 修改头像
    CHANG_AVATAR = 1
    # 修改简介
    CHANGE_ABOUT = 2
    # 发布视频
    PUBLISH_VIDEO = 3
    # 回复私信和评论
    REPLAY_INTERACT = 4
    # 养号
    YANG_HAO = 5


def main():
    DeviceScreen.init()
    # 初始化任务
    fetch_task = Task()
    engine_set_debug(True)
    action = TaskAction(fetch_task.task_action)
    task_app = fetch_task.ret_json.task_app
    # 授权抖音所有应用权限
    if task_app == "抖音":
        shell(f"curl http://127.0.0.1:9082/modifydev?cmd=18&pkg={dy_pkg}")
    elif task_app == "TikTok":
        shell(f"curl http://127.0.0.1:9082/modifydev?cmd=18&pkg={tiktok_pkg}")
    log_d("任务类型:", action)
    log_d("取到任务:", fetch_task)

    try:
        if action is TaskAction.PUBLISH_VIDEO:
            local_video_lit = shell("ls /sdcard/Download/").split('\n')
            video_name = os.path.basename(fetch_task.params['_file_video'])
            for name in local_video_lit:
                if name == video_name or not name:
                    continue
                need_remove_path = "/sdcard/Download/" + name
                shell('rm -f {0}'.format(need_remove_path))
                log_d('删除非目标文件 /sdcard/Download/{0}'.format(name))
            # 刷新媒体
            shell(
                "am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Download/" + video_name)
            dy.release_video(fetch_task, dy_pkg) if task_app == '抖音' else tiktok.release_video(fetch_task,
                                                                                                     tiktok_pkg)
        elif action is TaskAction.CHANG_NICKNAME:
            dy.update_nickname(fetch_task, dy_pkg) if task_app == '抖音' else tiktok.update_nickname(fetch_task,
                                                                                                     tiktok_pkg)
        elif action is TaskAction.CHANG_AVATAR:
            dy.update_avatar(fetch_task, dy_pkg) if task_app == '抖音' else tiktok.update_avatar(fetch_task,
                                                                                                     tiktok_pkg)
        elif action is TaskAction.CHANGE_ABOUT:
            dy.update_sign(fetch_task, dy_pkg) if task_app == '抖音' else tiktok.update_sign(fetch_task,
                                                                                                     tiktok_pkg)
        elif action is TaskAction.REPLAY_INTERACT:
            dy.interact(fetch_task, dy_pkg) if task_app == '抖音' else tiktok.interact(fetch_task,
                                                                                                     tiktok_pkg)
        elif action is TaskAction.YANG_HAO:
            dy.on_hook(fetch_task, dy_pkg) if task_app == '抖音' else tiktok.on_hook(fetch_task,
                                                                                       tiktok_pkg)
        else:
            fetch_task.update_task_status(TaskStatus.DEVICE_EXE_ERROR, f"工程未定义:{fetch_task.task_action}")
            return
    except Exception as ex:
        # 同时在脚本与数据库记错错误日志
        log_e(traceback.format_exc())
        fetch_task.update_task_status(TaskStatus.DEVICE_EXE_ERROR, f"代码错误: {(repr(ex))} | {traceback.format_exc()}")

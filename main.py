from task import *
import dy
import tiktok


def main():
    _task = Task()
    task_name = _task.ret_json
    task_app = _task.ret_json
    match task_name:
        case '修改昵称':
            dy.update_nickname(_task) if task_app == '抖音' else tiktok.update_nickname(_task)
        case '修改简介':
            dy.update_sign(_task) if task_app == '抖音' else tiktok.update_sign(_task)
        case '修改头像':
            dy.update_avatar(_task) if task_app == '抖音' else tiktok.update_avatar(_task)
        case '发布视频':
            dy.release_video(_task) if task_app == '抖音' else tiktok.release_video(_task)
        case '私聊与互动':
            dy.interact(_task) if task_app == '抖音' else tiktok.interact(_task)
        case '养号':
            dy.on_hook(_task) if task_app == '抖音' else tiktok.on_hook(_task)
        case _:
            task.update_task_status(TaskStatus.DEVICE_EXE_ERROR, "执行错误，任务不存在")

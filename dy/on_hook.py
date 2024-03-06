import time

from yyds import *
from dy.utils import control_click, set_text_,odds


def main(task_id, task_params) -> TaskRet:
    pkg = "com.ss.android.ugc.aweme"
    params = task_params
    # params = {
    #     "duration": 60,  # 养号时长，分钟
    #     "is_star": True,  # 是否随机点赞视频
    #     "is_comment": True,  # 是否随机评论
    #     "comment": "评论内容",  # 评论内容
    #     "is_concern": True,  # 是否随机关注用户
    #     "is_browse_comments": True,  # 是否随机浏览评论区
    #     "is_comments_star": True,  # 是否随机评论区点赞
    # }
    home_activity = ".splash.SplashActivity"
    engine_set_debug(True)
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(5)
    stop_time = time.time() + params["duration"] * 60
    try:
        while time.time() >= stop_time:
            if odds():
                # 随机点进用户里面去查看
                pass
            if params["is_star"] and odds():
                # 随机点赞
                pass
            if params["is_comment"] and odds():
                # 随机评论
                set_text_(params["comment"])
            if params["is_concern"] and odds():
                # 随机关注用户
                pass
            if params["is_browse_comments"] and odds():
                # 随机浏览评论区
                pass
            if params["is_comments_star"] and odds():
                # 随机评论区点赞
                pass
        return TaskRet(task_id, True, "养号结束")
    except Exception as e:
        log_d(e)
        return TaskRet(task_id, False, "异常中断")

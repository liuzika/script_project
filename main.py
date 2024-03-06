# import dy
# from yyds import *
import test_dy


def main():
    test_dy.yh(1)
    # device_id = shell("cat /data/local/tmp/id")
    # server_json = requests.get(f"http://xxxxxxx?deviceId=${device_id}").json()  # 此脚本被运行, 向服务器申请执行参数
    # task_name = server_json["task"]
    # task_params = server_json["params"]  # 一个嵌套的json, 包含具体的任务参数, 把每个json写出来到test代码里, 方便写接口
    # task_id = server_json["task_id"]
    # task_map = {
    #     "release_video": dy.release_video,  # 发布视频
    #     "update_sign": dy.update_sign,  # 修改简介
    #     "update_avatar": dy.update_avatar,  # 修改头像
    #     "update_nickname": dy.update_nickname,  # 修改昵称
    # }
    # ret: TaskRet = task_map[task_name](task_id, task_params)
    # requests.post("xxxxx", json=json.dumps(ret.__dict__))  # 向服务返回任务执行状态

import json

import tiktok


# 发布视频
def fbsp(task_id):
    params = {
        "desc": "冲冲冲冲",  # 视频描述
        "video": "",  # 视频
        "@user": ["肆无忌惮", "发胖子", "LZK", "叶子短剧"],  # 要@的用户名，可多个
        "tag": ["爆款短剧", "精彩短剧"],  # 视频标签、话题，可多个
        "address": "gd"  # 定位
    }
    ret = tiktok.release_video(task_id, params)
    print(json.dumps(ret.__dict__))


# 修改头像
def xgtx(task_id):
    params = {
        "url": "https://xxx.jpg/"  # 图片本地地址
    }
    ret = tiktok.update_avatar(task_id, params)
    print(json.dumps(ret.__dict__))


# 修改简介
def xgjj(task_id):
    params = {
        "sign": "xxxxxxxxxxxxxxxxxxxxxx"  # 简介，一段文本
    }
    ret = tiktok.update_sign(task_id, params)
    print(json.dumps(ret.__dict__))


# 修改昵称
def xgnc(task_id):
    params = {
        "nickname": "xxx"  # 新昵称
    }
    ret = tiktok.update_nickname(task_id, params)
    print(json.dumps(ret.__dict__))


# 养号
def yh(task_id):
    params = {
        "duration": 60,  # 养号时长，分钟
        "user_info": {"is": True, "odds": 10},  # 随机查看用户
        "star": {"is": True, "odds": 20},  # 是否随机点赞视频
        "comment": {"is": True, "odds": 20, "text": "评论内容"},  # 是否随机评论
        "concern": {"is": True, "odds": 10},  # 是否随机关注用户
        "browse_comments": {"is": True, "odds": 10, "is_star": True, "star_odds": 20},  # 是否随机浏览评论区
    }
    ret = tiktok.on_hook(task_id, params)
    print(json.dumps(ret.__dict__))


# 互动
def hd(task_id):
    params = {
        "text": "xxx"  # 新昵称
    }
    ret = tiktok.interact(task_id, params)
    print(json.dumps(ret.__dict__))

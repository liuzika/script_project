import json

import dy


# 发布视频
def fbsp(task_id):
    params = {
        "desc": "冲冲冲冲",  # 视频描述
        "video": "",  # 视频
        "@user": ["肆无忌惮", "发胖子", "LZK", "叶子短剧"],  # 要@的用户名，可多个
        "tag": ["爆款短剧", "精彩短剧"],  # 视频标签、话题，可多个
        "address": "gd"  # 定位
    }
    ret = dy.release_video(task_id, params)
    print(json.dumps(ret.__dict__))


# 修改头像
def xgtx(task_id):
    params = {
        "url": "https://xxx.jpg/"  # 图片地址
    }
    ret = dy.update_avatar(task_id, params)
    print(json.dumps(ret.__dict__))


# 修改简介
def xgjj(task_id):
    params = {
        "sign": "xxxxxxxxxxxxxxxxxxxxxx"  # 简介，一段文本
    }
    ret = dy.update_sign(task_id, params)
    print(json.dumps(ret.__dict__))


# 修改昵称
def xgnc(task_id):
    params = {
        "nickname": "xxx"  # 新昵称
    }
    ret = dy.update_nickname(task_id, params)
    print(json.dumps(ret.__dict__))


# 养号
def yh(task_id):
    params = {
        "duration": 60,  # 养号时长，分钟
        "is_star": True,  # 是否随机点赞视频
        "is_comment": True,  # 是否随机评论
        "comment": "评论内容",  # 评论内容
        "is_concern": True,  # 是否随机关注用户
        "is_browse_comments": True,  # 是否随机浏览评论区
        "is_comments_star": True,  # 是否随机评论区点赞
    }
    ret = dy.on_hook(task_id, params)
    print(json.dumps(ret.__dict__))


# 互动
def hd(task_id):
    params = {
        "text": "xxx"  # 新昵称
    }
    ret = dy.interact(task_id, params)
    print(json.dumps(ret.__dict__))
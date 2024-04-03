import tiktok


# 发布视频
def fbsp():
    params = {"params": {
        "desc": "冲冲冲冲",  # 视频描述
        "video": "",  # 视频
        "@user": ["肆无忌惮", "发胖子", "LZK", "叶子短剧"],  # 要@的用户名，可多个
        "tag": ["爆款短剧", "精彩短剧"],  # 视频标签、话题，可多个
        "address": "gd"  # 定位
    }}
    tiktok.release_video(params)


# 修改头像
def xgtx():
    params = {"params" : {
        "url": "https://xxx.jpg/"  # 图片本地地址
    }}
    tiktok.update_avatar(params)


# 修改简介
def xgjj():
    params = {"params": {
        "sign": "xxxxxxxxxxxxxxxxxxxxxx"  # 简介，一段文本
    }}
    tiktok.update_sign(params)


# 修改昵称
def xgnc():
    params = {"params": {
        "nickname": "xxx"  # 新昵称
    }}
    tiktok.update_nickname(params)


# 养号
def yh():
    params = {"params": {
        "duration": 60,  # 养号时长，分钟
        "user_info": {"is": True, "odds": 10},  # 随机查看用户
        "star": {"is": True, "odds": 20},  # 是否随机点赞视频
        "comment": {"is": True, "odds": 20, "text": "评论内容"},  # 是否随机评论
        "concern": {"is": True, "odds": 10},  # 是否随机关注用户
        "browse_comments": {"is": True, "odds": 10, "is_star": True, "star_odds": 20},  # 是否随机浏览评论区
    }}
    tiktok.on_hook(params)


# 互动
def hd():
    params = {"params": {
        "text": "xxx"  # 新昵称
    }}
    tiktok.interact(params)

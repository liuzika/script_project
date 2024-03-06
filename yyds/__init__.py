from .auto_plus import *


class TaskRet:
    def __init__(self, uuid, success: bool, desc: str) -> None:
        self.uuid = uuid
        self.success = success
        self.desc = desc

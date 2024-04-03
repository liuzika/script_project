from enum import Enum

from .auto_plus import *


class TaskStatus(Enum):
    # 手机正在执行中
    DEVICE_EXE = 5
    # 手机执行完成
    DEVICE_FINISH = 7
    # 手机执行异常
    DEVICE_EXE_ERROR = 9

import random

from yyds import *


def control_click(s=3, **node) -> None:
    """
    查找控件并点击
    :param s: 等待几秒
    :param node: 匹配参数
    :return: none
    """
    res = ui_match(**node)
    if len(res):
        lists = res[0].bound_str.replace("][", ",")[1:-1].split(",")
        x = int(lists[0]) + ((int(lists[2]) - int(lists[0])) / 2)
        y = int(lists[1]) + ((int(lists[3]) - int(lists[1])) / 2)
        click(int(x), int(y))
    sleep(s)


def set_text_(text) -> None:
    set_yy_input_enable(True)
    x_input_clear()
    sleep(1)
    set_yy_input_enable(True)
    x_input_clear()
    sleep(1)
    set_yy_input_enable(True)
    x_input_text(text)
    sleep(1)


def odds(o=25) -> bool:
    """
    获取概率
    :param o: 概率0~100，默认25
    :return: bool
    """
    return random.randint(1, 100) <= o

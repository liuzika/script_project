from yyds import *


def control_click(s=3, node=None, **match_params) -> bool:
    """
    查找控件并点击
    :param s: 等待几秒
    :param node: None
    :param match_params: 匹配参数
    :return: bool
    """
    lists = []
    if node:
        lists = node.bound_str.replace("][", ",")[1:-1].split(",")
    else:
        res = ui_match(**match_params)
        if len(res):
            lists = res[0].bound_str.replace("][", ",")[1:-1].split(",")
    if lists:
        x = int(lists[0]) + ((int(lists[2]) - int(lists[0])) / 2)
        y = int(lists[1]) + ((int(lists[3]) - int(lists[1])) / 2)
        click(int(x), int(y))
        sleep(s)
        return True
    else:
        return False


def set_text_(text) -> None:
    set_yy_input_enable(True)
    x_input_clear()
    x_input_clear()
    sleep(1)
    set_yy_input_enable(True)
    x_input_text(text)
    sleep(1)


def odds(o=20) -> bool:
    return random.randint(1, 100) <= o


def try_func(fun):
    def wrapper(task, pkg):
        try:
            engine_set_debug(True)
            fun(task, pkg)
        except Exception as e:
            task.update_task_status(TaskStatus.DEVICE_EXE_ERROR, f"执行错误: {repr(e)}")

    return wrapper

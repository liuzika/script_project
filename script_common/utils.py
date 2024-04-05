from yyds import *


# 点击获取第一个符合条件的控件
def click_ui_find_one(s=3, node=None, desc='', **match_params) -> bool:
    try:
        flag = False
        if node:
            click_target(node)
            flag = True
        ret = ui_match(visible_to_user="true", limit=1, **match_params)
        if len(ret):
            click_target(ret[0])
            flag = True
        if flag:
            log_d('点击', desc)
            sleep(s)
        return flag
    except Exception as e:
        return False


def deep_get_child_node(node: Node, resource_id: str, text: str or int = 0) -> None or Node:
    """
    递归获取符合条件的子节点
    :param text:
    :param node:
    :param resource_id:
    :return:
    """
    try:
        if node is None:
            return None
        child_list = ui_child(node)
        for child in child_list:
            if child.id == resource_id and (text == 0 or re.match(text, child.text)):
                return child
            elif len(ui_child(child)):
                node = deep_get_child_node(child, resource_id, text)
                if node is not None:
                    return node
    except Exception as e:
        return None


def click_random_widget(**match_params) -> bool:
    """
    随机点击符合条件的控件
    :param match_params:
    :return:
    """
    try:
        widget = ui_match(visible_to_user="true", **match_params)
        count = len(widget)
        if count:
            random_index = int(count / 2)
            item = widget[random_index]
            log_d(item)
            for k in match_params.keys():
                if k == 'text':
                    log_d('点击', item.text)
                elif k == 'content_desc':
                    log_d('点击', item.desc)
            click_target(item)
            return True
        return False
    except Exception as e:
        log_e(e)
        return False


# 获取第一个符合条件的控件
def ui_find_one(**match_params) -> Node or None:
    try:
        return ui_match(visible_to_user="true", limit=1, **match_params)[0]
    except Exception as e:
        return None


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
        for i in range(3):
            if fun(task, pkg):
                break

    return wrapper


def split(text) -> List[str]:
    return re.split("[,，]", text)


def start_app(pkg):
    stop_app(pkg)
    sleep(2)
    open_app(pkg)
    sleep(5)

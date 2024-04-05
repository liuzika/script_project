import sys
import time


def format_time():
    """
    获取格式化的时间, 格式样式如:2024.02.04 12:56:31
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


class Logger:
    log_path = f"/sdcard/Documents/{time.strftime('%Y-%m-%d', time.localtime())}.log"

    @classmethod
    def log_d(cls, *objs):
        """
        打印标准日志, 在Yyds.Auto开发插件中一般日志显示为灰色
        """
        lt = format_time() + "\t" + " ".join([str(i) for i in objs])
        print(lt, file=sys.stdout)
        with open(cls.log_path, mode="a+") as fw:
            fw.write("D:" + lt + "\n")
            fw.flush()

    @classmethod
    def log_e(cls, *objs):
        """
        打印错误日志, 在Yyds.Auto开发插件中一般日志显示为红色
        """
        lt = format_time() + "\t" + " ".join([str(i) for i in objs])
        print(lt, file=sys.stderr)
        with open(cls.log_path, mode="a+") as fw:
            fw.write("E:" + lt  + "\n")
            fw.flush()

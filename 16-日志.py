import logging,colorlog
from colorama import Fore,Style

#https://blog.csdn.net/u013769085/article/details/119668355

class logger():
    def __init__(self):
        self.logger = logging.getLogger(__file__)#创建一个总记录器
        self.logger.setLevel(logging.DEBUG)#设置日志等级总开关

        # 设置日志格式
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s]-%(message)s",datefmt="%Y-%m-%d %H:%M:%S")

        # 建立一个filehandler来把日志记录在文件里，级别为debug以上
        fh = logging.FileHandler("16_log.txt",'a+',encoding='utf-8')
        fh.setLevel(logging.WARNING)
        fh.setFormatter(formatter)

        # 建立一个streamhandler来把日志打在CMD窗口上
        "black""red""green""yellow""blue""purple""cyan""white"
        log_colors_config = {
                    'DEBUG': 'light_blue',
                    'INFO': 'light_green',
                    'WARNING': 'light_yellow',
                    'ERROR': 'light_red',
                    'CRITICAL': 'light_purple',
                }
        formatter = colorlog.ColoredFormatter('%(log_color)s[%(asctime)s] [%(levelname)s]- %(message)s',datefmt="%Y-%m-%d %H:%M:%S",log_colors=log_colors_config)  # 日志输出格式
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)

        #将相应的handler添加在logger对象中
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def returnLogger(self):
        # 返回logger句柄
        return self.logger
logger=logger().returnLogger()
if __name__ == '__main__':
    # 开始打日志
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")



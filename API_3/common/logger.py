import logging
from API_3.common import constants


def get_logger(name):
    mylogger = logging.getLogger(name)
    # 进行优化，将日志级别放到配置文件中
    mylogger.setLevel("DEBUG")
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d]"
    formatter = logging.Formatter(fmt=fmt)

    console_handler = logging.StreamHandler()
    console_handler.setLevel("DEBUG")
    console_handler.setFormatter(formatter)
    mylogger.addHandler(console_handler)

    file_handler = logging.FileHandler(constants.log_dir)
    file_handler.setLevel("DEBUG")
    file_handler.setFormatter(formatter)
    mylogger.addHandler(file_handler)

    return mylogger


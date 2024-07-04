# #coding=utf-8
'''
   日志记录类
   1，按天分割文件
   2，使用方法：DayLogger("test.txt", level='debug')，只需要传入日志文件名就可以，默认会出现在当前的log目录中，如果目录不存在则自动创建
   3，调用方法： logger.logger.error('报错')    需要注意这里有两个logger哦
   ----by 丁毅
      2021-03-08
'''

import logging,os  # 引入logging模块
from logging import handlers

class DayLogger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射


    def __init__(self,filename,level='info',when='MIDNIGHT',backCount=7,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        #检查当前目录是否存在log目录，如果不存在则创建
        if(os.path.isdir("./log")!=True):
            os.mkdir("log")
        filename = os.path.join("./log/", filename)
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往控制台输出
        sh.setFormatter(format_str) #设置控制台上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,interval=1,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.suffix = "%Y-%m-%d.log" #设置文件后缀
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
if __name__ == '__main__':
    #logger = Logger('all.log',level='debug')
    # filename = setting.now_time+ ".txt"
    # logfile = os.path.join(setting.logs_path,filename)
    # logger = Logger(logfile,level='debug')

    logger = DayLogger("test.txt", level='debug')
    logger=logger.logger;
    logger.debug('debug') # 括号内的内容即为日志的文本内容
    logger.info('info')
    logger.warning('警告')
    logger.error('报错')
    logger.critical('严重')
    #Logger('error.log', level='error').logger.error('error')

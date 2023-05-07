# gunicorn_conf.py
# gunicorn的配置文件必须为一个python文件，只是将命令行中的参数写进py文件中而已，如果需要设置哪个参数，则在py文件中为该参数赋值即可。
import os

import gevent.monkey
gevent.monkey.patch_all()
import multiprocessing


current_work_dir = os.getcwd()            # 当前执行gunicorn命令的目录
print('current_work_dir ---->  ', current_work_dir)
# gunicorn工作目录，下面日志目录都是基于工作目录的相对路径
chdir=current_work_dir

# 每次启动会显示，配置参数，生产环境可以设置为False
debug = False

# ip和端口绑定
bind = "0.0.0.0:5022"

# 启动的进程数
workers = int(multiprocessing.cpu_count() / 2) + 1
# workers = int(multiprocessing.cpu_count() * 2) + 1
# 每个worker进程开启的线程数
threads = 2
# 工作模式设置为gevent协程
worker_class = 'gevent'
# 单个线程的协程数量
worker_connections = 100

# 监听队列，最大挂起的连接数
backlog = 512

# 日志记录等级
loglevel = 'debug'
# 接入服务的日志记录文件
accesslog = "logs/gunicorn_access.log"         # 日志路径，从执行gunicorn命令的当前目录开始，若指定chdir，则相对于chdir
# 启动和调用出现错误日志文件
errorlog = "logs/gunicorn_debug.log"
# 日志格式
# access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'

# master进程id文件，kill掉该id，gunicorn就停止运行
pidfile = "logs/gunicorn.pid"

# 设置守护进程，后台启动，默认False
# 当supervisor启动gunicorn时，不要设置为True，会导致状态为backoff或fatal
# daemon = True




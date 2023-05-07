import os


class AppDefaultConfig:
    """
    配置
    """
    # flask配置
    SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'
    DEBUG = False

    # MQ连接
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST') or '192.168.1.7'
    RABBITMQ_PORT = os.getenv('RABBITMQ_PASSWORD') or 5672
    RABBITMQ_V_HOST = os.getenv('RABBITMQ_V_HOST') or '/default'
    RABBITMQ_USERNAME = os.getenv('RABBITMQ_USERNAME') or 'zeng'
    RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD') or '123456'

    # ETCD连接
    ETCD_HOST = os.getenv('ETCD_HOST') or '192.168.1.7'
    ETCD_PORT = os.getenv('ETCD_PASSWORD') or 2379
    ETCD_USERNAME = os.getenv('ETCD_USERNAME') or 'huang'
    ETCD_PASSWORD = os.getenv('ETCD_PASSWORD') or 'Root123456'

    # 队列定义
    receive_topic = {
        'model_type': 'direct',
        'exchange_name': 'alg-server.default_receive_topic.exchange',
        'routing_key': 'alg-server.default_receive_topic.route',
        'queue': 'alg-server.default_receive_topic.queue',
    }

    send_topic = {
        'model_type': 'direct',
        'exchange_name': 'alg-server.default_send_topic.exchange',
        'routing_key': 'alg-server.default_send_topic.route',
        'queue': 'alg-server.default_send_topic.queue',
    }

    # 监听队列
    QUEUE_RECEIVE_MODEL_TYPE = os.getenv('QUEUE_RECEIVE_MODEL_TYPE') or receive_topic['model_type']
    QUEUE_RECEIVE_EXCHANGE = os.getenv('QUEUE_RECEIVE_EXCHANGE') or receive_topic['exchange_name']
    QUEUE_RECEIVE_ROUTING_KEY = os.getenv('QUEUE_RECEIVE_ROUTING_KEY') or receive_topic['routing_key']
    QUEUE_RECEIVE_QUEUE = os.getenv('QUEUE_RECEIVE_QUEUE') or receive_topic['queue']

    # 发送队列
    QUEUE_SEND_MODEL_TYPE = os.getenv('QUEUE_SEND_MODEL_TYPE') or send_topic['model_type']
    QUEUE_SEND_EXCHANGE = os.getenv('QUEUE_SEND_EXCHANGE') or send_topic['exchange_name']
    QUEUE_SEND_ROUTING_KEY = os.getenv('QUEUE_SEND_ROUTING_KEY') or send_topic['routing_key']
    QUEUE_SEND_QUEUE = os.getenv('QUEUE_SEND_QUEUE') or send_topic['queue']


AppConfig = AppDefaultConfig

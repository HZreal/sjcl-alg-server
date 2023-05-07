import json
import threading

import pika
from pika import BlockingConnection

from consumer.default_consumer import default_callback
from utils.log import logger
from core.f_app import app


class RabbitMQProxy:
    def __init__(self):
        self.rabbitmq_server_host = app.config['RABBITMQ_HOST']
        self.rabbitmq_server_port = app.config['RABBITMQ_PORT']
        self.rabbitmq_server_v_host = app.config['RABBITMQ_V_HOST']
        self.rabbitmq_server_username = app.config['RABBITMQ_USERNAME']
        self.rabbitmq_server_password = app.config['RABBITMQ_PASSWORD']

        self._connection: BlockingConnection = None
        self._channel = None

        self.init()

        print(self.rabbitmq_server_host, self.rabbitmq_server_port, self.rabbitmq_server_username,
              self.rabbitmq_server_password, self.rabbitmq_server_v_host)

    def init(self):
        """

        :return:
        """
        self.validate()
        self.connect()

    def validate(self):
        """

        :return:
        """
        assert not (
                (self.rabbitmq_server_username is None) ^ (
                self.rabbitmq_server_password is None)), 'Specify username and password or both not'

    def connect(self):
        """

        :return:
        """
        if not (self.rabbitmq_server_username and self.rabbitmq_server_password):
            # 无需认证
            self._connection = pika.BlockingConnection(pika.ConnectionParameters(
                self.rabbitmq_server_host,
                self.rabbitmq_server_port,
                self.rabbitmq_server_v_host
            ))
        else:
            # 需认证
            credentials = pika.PlainCredentials(
                self.rabbitmq_server_username,
                self.rabbitmq_server_password
            )
            self._connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    self.rabbitmq_server_host,
                    self.rabbitmq_server_port,
                    self.rabbitmq_server_v_host,
                    credentials=credentials
                ))

        self._channel = self._connection.channel()

    def get_channel(self):
        """
        自定义一个新channel
        :return:
        """
        return self._connection.channel()

    def _bind(self):
        """

        :return:
        """

    def _basic_direct_send(
            self,
            msg: str = None,
            exchange_name=app.config['QUEUE_SEND_EXCHANGE'],
            routing_key=app.config['QUEUE_SEND_ROUTING_KEY'],
    ):
        """

        :param exchange_name:
        :param routing_key:
        :param msg:
        :return:
        """
        new_channel = self.get_channel()
        new_channel.basic_publish(exchange=exchange_name, routing_key=routing_key,
                                    body=bytes(msg, encoding="utf8"))

        logger.info(" --- Send message over ! ")
        new_channel.close()

    def send(self, msg: str):
        """

        :return:
        """


    def send_json(self, msg: str):
        """

        :return:
        """
        self._basic_direct_send(msg=msg)

    def _start_consume(
            self,
            queue=app.config['QUEUE_RECEIVE_QUEUE'],
            exchange=app.config['QUEUE_RECEIVE_EXCHANGE'],
            routing_key=app.config['QUEUE_RECEIVE_ROUTING_KEY'],
            callback=default_callback,
            **kwargs
    ):
        """
        默认启动一个direct模式的消费
        :param queue:
        :param exchange:
        :param routing_key:
        :param callback:
        :param kwargs: 备用参数
        :return:
        """
        print('----------', exchange, routing_key, queue)
        self._channel.exchange_declare(exchange=exchange)
        self._channel.queue_declare(queue=queue)
        self._channel.queue_bind(queue=queue, exchange=exchange, routing_key=routing_key)
        self._channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        self._channel.start_consuming()

    def close(self):
        self._connection.close()

    def run(self):
        """

        :return:
        """
        t = threading.Thread(target=self._start_consume)
        t.setDaemon(True)
        t.start()
        logger.info(" --- The RabbitMQ application is consuming --- ")

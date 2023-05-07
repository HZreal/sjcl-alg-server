from core.f_app import app
import etcd3


class EtcdProxy:
    def __init__(self):
        """

        """
        self.etcd_host = app.config['ETCD_HOST']
        self.etcd_port = app.config['ETCD_PORT']
        self.etcd_username = app.config['ETCD_USERNAME']
        self.etcd_password = app.config['ETCD_PASSWORD']
        self.client = etcd3.client(self.etcd_host, self.etcd_port, self.etcd_username, self.etcd_password)

        #
        self.register()

    def register(self):
        """

        :return:
        """
        self.put('register', 'ip   port')

    def put(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        self.client.put(key, value)

    def get(self, key):
        """

        :param key:
        :return:
        """
        return self.client.get(key)

from core.etcd_proxy import EtcdProxy
from core.rabbitMQ_proxy import RabbitMQProxy
from core.f_app import app

mq = RabbitMQProxy()
etcd = EtcdProxy()

def start():
    # 挂载
    app.mq = mq

    app.etcd = etcd

    app.mq.run()
    app.run('0.0.0.0', 5001)



if __name__ == '__main__':
    start()

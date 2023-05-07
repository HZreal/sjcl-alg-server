import json

from alg.alg import invoke_alg
from core.f_app import app


def default_callback(ch, method, properties, body):
    """

    :param ch:
    :param method:
    :param properties:
    :param body: 字节类型
    :return:
    """
    print(' --- data received from MQ------------------> ', str(body, encoding="utf-8"))

    alg_input = str(body, encoding="utf-8")

    result = invoke_alg(alg_input)

    app.mq.send_json(json.dumps({'alg_result': result}))


def callback(ch, method, properties, body):
    """

    :param ch:
    :param method:
    :param properties:
    :param body:
    :return:
    """

    print(' --- data received ------------------> ', body)

    alg_input = str(body, encoding="utf-8")

    result = invoke_alg(alg_input)


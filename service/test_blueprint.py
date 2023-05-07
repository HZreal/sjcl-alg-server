import json

from flask import Blueprint, current_app

test_bp = Blueprint('test', __name__)


@test_bp.route('/profile')
def get_profile():
    return 'user profile'


@test_bp.route('/login', methods=['POST'])
def login():
    return {'code': 0, 'msg': 'success', 'data': None}


@test_bp.route('/send', methods=['GET'])
def send():

    # 发送 mq 消息
    current_app.mq.send_json(json.dumps({'username': 'huang'}))

    return {'code': 0, 'msg': 'success', 'data': None}

from service import test_bp
from flask import Flask, jsonify
from config import AppConfig

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

# 加载配置
print(AppConfig)
app.config.from_object(AppConfig)

# 注册蓝图
app.register_blueprint(test_bp, url_prefix='/test')


@app.route('/')
def route_map():
    """
    查看所有url
    """
    rules_iterator = app.url_map.iter_rules()
    return jsonify(
        {rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')})

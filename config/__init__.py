import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


env = os.getenv('env') or os.getenv('ENV') or 'default'  # dev local prod 等
print('Environment ---->  ', env)
try:
    module = __import__('cfg_' + env)
    AppConfig = getattr(module, 'AppConfig')
except Exception as e:
    print('Specified AppConfig Loading Error  ---->  ', e)
    from config.cfg_default import AppConfig


__all__ = ['AppConfig']
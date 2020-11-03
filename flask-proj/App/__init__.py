from flask import Flask
from flask_script import Manager

from flask_migrate import MigrateCommand
from App.ext_init import init_ext, migrate
from App.settings import Development
from App.views import blue, init_api


# 初始化 APP模块
def create_app():
    # 创建 flask实例
    app = Flask(__name__)

    # 初始化接口
    init_api(app)

    # 加载配置
    app.config.from_object(Development)

    # 使用flask实例初始化各种扩展库, 目前已存在 sqlAlchemy
    init_ext(app)

    # 初始化manager对象
    manager = Manager(app=app)

    # 给manager对象添加 migrate 指令集
    manager.add_command('db', MigrateCommand)

    # 返回manager对象用以启动服务
    return manager

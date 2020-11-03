from App.ext_init import api
from App.views.restView import RestView
from .emailView import eBlue
from .flashView import fBlue
from .User import model_blue
from .index import blue
from .gVIew import gBlue


def init_api(app):
    # 在views.py中注册所有的蓝图实例, 这样使得模块划分更加规范
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=model_blue)
    app.register_blueprint(blueprint=gBlue)
    app.register_blueprint(blueprint=fBlue)
    app.register_blueprint(blueprint=eBlue)

    # 在 flask-restful 实例上注册路由
    # 路由中设置参数的方式同flask
    api.add_resource(RestView, '/rest/<string:name>/')

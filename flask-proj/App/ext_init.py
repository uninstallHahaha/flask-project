# 该文件使用 flask实例 统一初始化各种扩展库
from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# 创建SQLAlchemy实例
models = SQLAlchemy()
# 创建flask-migrate实例
migrate = Migrate()
# 创建flask-cache实例
cache = Cache(config={'CACHE_TYPE': 'simple'})
# 创建flask-mail实例
mail = Mail()
# 初始化 flask-restful实例
api = Api()


# 初始化各种插件
def init_ext(app):
    # 初始化SQLAlchemy实例及数据模型,使用flask实例初始化SQLAlchemy实例
    models.init_app(app)

    # 使用flask实例和sqlAlchemy实例初始化flask-migrate实例
    migrate.init_app(app, models)

    # 初始化 flask-session , 没开 redis, 所以不初始化flask-session
    # Session(app)

    # 初始化 flask-bootstrap
    Bootstrap(app)

    # 初始化 flask-DebugToolbar
    DebugToolbarExtension(app)

    # 初始化 flask-cache
    cache.init_app(app)

    # 初始化 flask-mail
    mail.init_app(app)

    # 初始化 flask-restful
    api.init_app(app)

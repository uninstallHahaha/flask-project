# 开发环境配置, 该文件中应当包含多套环境配置, 以满足不同的需求
class Development:
    # 开启调试模式
    DEBUG = True

    # SqlALCHEMY 配置
    # 数据库uri格式: 数据库+驱动//用户名:密码@主机:端口/库名
    # mysql的格式就是: mysql+pymysql://用户名:密码@localhost:3306/库名
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 设置session
    SECRET_KEY = 'suibianxiedianshenme'
    # 设置session 存到 redis 中
    SESSION_TYPE = 'redis'

    # 设置 flask-mail
    MAIL_SERVER = 'smtp.163.com'  # 163邮箱域名
    MAIL_PORT = 25  # 163 邮箱服务器端口
    MAIL_USERNAME = 'z2234261505@163.com' # 发送者账号
    MAIL_PASSWORD = 'IFKMTWLYEIBJDPXV'  # 这个就是生成的授权码
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

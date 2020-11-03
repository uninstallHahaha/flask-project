from flask import Blueprint, g, current_app

# 使用 g 保存全局数据示例
# 获取 config 数据示例
gBlue = Blueprint('gBlue', __name__, url_prefix='/g')


# 在 hook 函数中保存数据到 g 中
@gBlue.before_request
def set_g():
    g.msg = 'global data'


# 在其他接口中使用 g 中保存的数据
@gBlue.route('/get_g/')
def get_g():
    return 'get g data: %s' % g.msg


# 获取 config 数据
@gBlue.route('/get_config/')
def get_config():
    config = current_app.config
    for key in config.keys():
        print(key, config[key])
    return 'get config'

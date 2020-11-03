from flask import Blueprint, render_template, redirect, url_for, request, make_response, Response, abort, session

from App.ext_init import cache
from App.models import models, User

# 本模块为接口相关的示例

blue = Blueprint('blue', __name__)


# 测试接口
@blue.route('/')
def index():
    return render_template('index.html', msg="内容")


# 使用缓存
@blue.route('/index_with_cache/')
@cache.cached(timeout=60)
def index_with_cache():
    print('cache接口')  # 使用了cache的接口只会在第一次执行方法中的内容,之后会使用缓存
    return '使用了flask-caching的接口'


# 接收参数, 默认转化为 string类型
@blue.route('/<con>/')
def get_param_def(con):
    return render_template('index.html', msg=con)


# 可限定类型 int, float, string(默认), uuid, path, any(a,b) 只接受列出的值
# 接收参数, 并指定接收参数的类型, 不是这个类型的请求不接受
@blue.route('/<int:con>/')
def get_param(con):
    return render_template('index.html', msg=con)


# 一个方法可以加多个路径装饰器
@blue.route('/get_var/<int:con>/')
@blue.route('/get_var/<string:con>/')
def get_var(con):
    return render_template('index.html', msg=con)


# 默认只支持 get, head, options 请求
# 通过设置 methods 指定支持的请求方式
@blue.route('/methods/', methods=['GET', 'POST', 'DELETE'])
def methods():
    return '支持多种方式的请求'


# 重定向
@blue.route('/redirect/')
def red():
    # 硬编码的路径
    # return redirect('/')
    # 使用 url_for() 反向解析的方式指定路径, 格式为: 蓝图实例名.方法名
    # return redirect(url_for('blue.index'))
    # 使用反向解析并传递参数, 直接在参数列表中以关键字参数的方式传参数
    return redirect(url_for('blue.get_var', con=123))


# request, 直接导包使用, 该对象属性值不能修改
@blue.route('/get_request/')
def get_request():
    return request.host


# 测试 ORM 操作
@blue.route('/add_user_index/')
def add_user():
    user = User()
    user.username = 'alice'
    # ORM 之保存
    models.session.add(user)
    models.session.commit()
    return '添加成功'


# 使用 SqlAlchemy实例创建数据表接口
@blue.route('/create_db/')
def create_db():
    models.create_all()
    return '创建成功'


# 删除 SqlAlchemy实例上数据表的接口
@blue.route('/drop_db/')
def drop_db():
    models.drop_all()
    return '删除成功'


# 返回 response
@blue.route('/get_response/')
def get_response():
    response = make_response('this is response', 201)
    return response


# 返回 response
@blue.route('/get_response_res/')
def get_response_res():
    response = Response('this is response', 201)
    return response


# 直接返回错误码
@blue.route('/get_error_code/')
def get_error_code():
    return abort(403)


# 定制错误页面
@blue.errorhandler(403)
def page_for_403(e):
    return "啊哦 403 没有登录"


# 设置 cookies
@blue.route('/set_cookies/')
def set_cookies():
    response = Response("设置 cookies 成功")
    response.set_cookie('name', 'alice')
    return response


# 获取 cookies
@blue.route('/get_cookies/')
def get_cookies():
    name = request.cookies.get('name') or ''
    return '获取到cookie的值为:%s' % name


# 设置 session
@blue.route('/set_session/')
def set_session():
    session['name'] = 'alice'
    return '设置 session 成功'


# 获取 session
@blue.route('/get_session/')
def get_session():
    return '获取到的 session值为: %s' % session.get('name')


# 返回使用了 bootstrap 的页面
@blue.route('/get_bootstrap_page/')
def get_bootstrap_page():
    return render_template('bootstrap_simple_page.html')

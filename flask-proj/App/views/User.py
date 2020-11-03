from flask import Blueprint

# 本模块为 orm 操作实例
from App.ext_init import models
from App.models import User

model_blue = Blueprint('model_blue', __name__)


# 添加一个
@model_blue.route('/add_user/')
def add_user():
    user = User()
    user.username = 'alice'
    models.session.add(user)
    models.session.commit()
    return 'model op : add user success'


# 添加一组
@model_blue.route('/add_users/')
def add_users():
    users = []
    for i in range(10):
        user = User()
        user.username = 'alice %s' % i
        users.append(user)
    models.session.add_all(users)
    models.session.commit()
    return 'model op : add users success'


# 更新一个
@model_blue.route('/update_user/')
def update_user():
    user = User.query.first()
    user.username = 'vlice'
    models.session.add(user)
    models.session.commit()
    return 'model op : update user success'


# 删除一个
@model_blue.route('/del_user/')
def del_user():
    user = User.query.first()
    models.session.delete(user)
    models.session.commit()
    return 'model op : del user success'

# 查询
# 类名.query.xxx
# xxx 可以是:
# xxx 的所有操作都是 BaseQuery 的父类 query 中的方法, BaseQuery 的 __str__方法为返回当前查询的sql语句
# all() 所有, 返回 list, 其他的接口都返回 BaseQuery类型, 所以如果all()了,那么就不能继续链式调用了
# first() 第一个
# get_or_404(id) 根据id返回值或者404错误
# get(id) 根据id返回值或者None
# filter(类名.属性名.__运算符方法名__('xxx'))
# ## ## 查询等于 filter(类名.属性名.__eq__('xxx'))
# ## ## 查询小于 filter(类名.属性名.__lt__('xxx'))
# ## ## 查询包含 filter(类名.属性名.contains('xxx'))
# ## ## 查询开头 filter(类名.属性名.startwith('xxx'))
# ## ## 模糊查询 filter(类名.属性名.like('xxx'))
# ## ## 组合条件 filter(and_(条件1, 条件2))
# ## ## 组合条件 filter(or_(条件1, 条件2))
# ## ## 组合条件 filter(not_(条件))
# filter(类名.属性名 数学运算符 值)
# filter_by(属性名 = 值)
# offset(n) 偏移n开始查, offset+limit 分页
# limit(n) 限制查询数目
# order_by('属性 或 -属性') 根据属性正反序排序 , 必须在 offset 和 limit 前使用

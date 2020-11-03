from flask_restful import Resource, fields, marshal_with, abort
from App.models import User

# 定义序列化规则
# user对象的序列化规则
user_fields = {
    'id': fields.Integer,
    'username': fields.String
}
# 要返回对象的序列化规则, 返回的对象中包含了user对象, 所以使用Nested来级联user的规则
res_fields = {
    'state': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(user_fields)
}
# 返回的数据中包含list数据的序列化规则
list_res_fields = {
    'msg': fields.String,
    'data': fields.List(fields.Nested(user_fields))
}


# 使用 flask-restful 定义的类视图
class RestView(Resource):
    # 接收参数
    def get(self, name):
        return {'name': name}

    # 未经序列化的对象数据无法直接传输
    # 使用marshal_with装饰器设置序列化规则用以序列化返回的数据
    @marshal_with(res_fields)
    def post(self, name):
        user = User()
        user.username = 'alice'
        user.id = 1
        res = {
            'state': 200,
            'msg': 'post success',
            'data': user
        }
        return res

    # 如果返回的数据包含list, 那么使用field.List() 来定义序列化规则
    @marshal_with(list_res_fields)
    def put(self, name):
        user_list = []
        for i in range(10):
            user = User()
            user.username = 'alice' + str(i)
            user_list.append(user)
        list_res = {
            'msg': 'ok',
            'data': user_list
        }
        return list_res

    # flask-restful 中的 abort 扩展了 flask 中的 abort, 可定义错误提示
    # 调用 abort 时传递的关键字参数都会作为错误提示的 key 和 value 返回
    def patch(self, name):
        # abort(错误码, 错误提示)
        abort(400, msg='自定义的错误提示1', message='自定义的错误提示2')

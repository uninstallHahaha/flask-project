from datetime import datetime

from App.ext_init import models


# 创建模型
class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(16))


# 该模型为 Student的外键模型
class Grade(models.Model):
    g_id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    g_name = models.Column(models.String(16))


# 创建模型, 该模型为模型属性示例
class Student(models.Model):
    # 生成表的名字
    __tablename__ = 'student'
    # 主键, 自增
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    # 唯一
    s_name = models.Column(models.String(16), unique=True)
    # 可为空
    s_des = models.Column(models.String(100), nullable=True)
    # 时间类型, 默认当前时间
    s_time = models.Column(models.DateTime, nullable=False, default=datetime.utcnow)
    # 定义外键
    s_grade = models.Column(models.Integer, models.ForeignKey(Grade.g_id))

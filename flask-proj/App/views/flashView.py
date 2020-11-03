from flask import Blueprint, redirect, url_for, flash, request, render_template

fBlue = Blueprint('fBlue', __name__, url_prefix='/flash')


# 假设这是一个登录接口
@fBlue.route('/show_flash/', methods=['GET', 'POST'])
def show_flash():
    # 返回登录页面
    if request.method == 'GET':
        return render_template('flash_notice.html')
    # 接收登录请求并返回登录失败的消息
    if request.method == 'POST':
        flash('登录失败')
        return redirect(url_for('fBlue.show_flash'))

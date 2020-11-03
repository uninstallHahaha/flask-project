from werkzeug.security import generate_password_hash, check_password_hash


# 使用hash加密的方式加密密码
def password_secret(password):
    return generate_password_hash(password)


# 使用hash解密的方式验证密码
def check_password(password, truepass):
    return check_password_hash(password, truepass)

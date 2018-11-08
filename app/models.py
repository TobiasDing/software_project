# coding:utf8

from datetime import datetime
from app import db

class User(db.Model):
    """用户数据模型"""

    __tablename__ = "user"  # 数据表名
    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(100), unique=True)
    info = db.Column(db.Text)  # 个性签名
    face = db.Column(db.String(255), unique=True)  # 头像
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    user_logs = db.relationship("UserLog", backref="user")  # 用户日志关联
    user_comments = db.relationship("Comment", backref="user")  # 用户评论关联
    user_collections = db.relationship("Collection", backref="user")  # 用户收藏关联

    def __repr__(self):
        return f"<User {self.name}>"


class UserLog(db.Model):
    """用户登录日志"""

    __tablename__ = "user_log"
    id = db.Column(db.Integer, primary_key=True)  # 日志编号
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 日志所属用户编号
    ip = db.Column(db.String(100))  # 登录IP
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 日志添加时间

    def __repr__(self):
        return f"UserLog {self.id}"


class Tag(db.Model):
    '''标签'''

    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 标签编号
    name = db.Column(db.String(100), unique=True)  # 标签名称
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 标签添加时间
    movies = db.relationship("Movie", backref="tag")  # 电影关联

    def __repr__(self):
        return f"<Tag {self.name}>"


class Movie(db.Model):
    '''电影'''

    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 电影编号
    title = db.Column(db.String(255), unique=True)  # 电影名称
    url = db.Column(db.String(255), unique=True)  # 电影地址
    info = db.Column(db.Text)  # 电影简介
    pic = db.Column(db.String(255), unique=True)  # 电影封面
    star = db.Column(db.SmallInteger)  # 电影评级
    play_count = db.Column(db.BigInteger)  # 播放量
    comment_num = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))  # 电影所属标签
    area = db.Column(db.String(255))  # 制片地区
    release_time = db.Column(db.Date)  # 上映时间
    len = db.Column(db.String(100))  # 电影长度
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 电影添加时间
    movie_comments = db.relationship("Comment", backref="movie")  # 电影评论关联
    movie_collections = db.relationship("Collection", backref="movie")  # 电影收藏关联

    def __repr__(self):
        return f"<Movie {self.title}>"


class Preview(db.Model):
    '''预告'''

    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)  # 预告编号
    title = db.Column(db.String(255), unique=True)  # 电影名称
    pic = db.Column(db.String(255), unique=True)  # 电影封面
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 预告添加时间

    def __repr__(self):
        return f"<Preview {self.title}>"


class Comment(db.Model):
    '''评论'''

    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # 评论编号
    content = db.Column(db.Text)  # 评论内容
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 评论所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 评论所属用户
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 评论时间

    def __repr__(self):
        return f"<Comment {self.id}>"


class Collection(db.Model):
    '''收藏'''

    __tablename__ = "collection"
    id = db.Column(db.Integer, primary_key=True)  # 收藏编号
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 收藏电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 收藏所属用户
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 收藏时间

    def __repr__(self):
        return f"<Comment {self.id}>"


class Authority(db.Model):
    '''权限管理'''

    __tablename__ = "authority"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)  # 地址
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 权限添加时间

    def __repr__(self):
        return f"<Authority {self.name}>"


class Role(db.Model):
    '''角色'''

    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    authorities = db.Column(db.String(1000))  # 权限列表
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    admin_roles = db.relationship("Admin", backref="role")

    def __repr__(self):
        return f"<Role {self.name}>"


class Admin(db.Model):
    '''管理员'''

    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)  # 0为超级管理员
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))  # 所属角色
    admin_logs = db.relationship("AdminLog", backref="admin")  # 管理员登录日志关联
    op_logs = db.relationship("OpLog", backref="admin")  # 管理员操作日志关联

    def __repr__(self):
        return f"<Admin {self.name}>"

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


class AdminLog(db.Model):
    """管理员登录日志"""

    __tablename__ = "admin_log"
    id = db.Column(db.Integer, primary_key=True)  # 日志编号
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 日志所属管理员编号
    ip = db.Column(db.String(100))  # 登录IP
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 日志添加时间

    def __repr__(self):
        return f"AdminLog {self.id}"


class OpLog(db.Model):
    """管理员登录日志"""

    __tablename__ = "op_log"
    id = db.Column(db.Integer, primary_key=True)  # 日志编号
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 操作所属管理员编号
    ip = db.Column(db.String(100))  # 登录IP
    reason = db.Column(db.String(600))  # 操作原因
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 日志添加时间

    def __repr__(self):
        return f"OpLog {self.id}"


# if __name__ == '__main__':
#     # db.create_all()
#     '''
#     role = Role(
#         name="超级管理员",
#         authorities=""
#     )
#
#     db.session.add(role)
#     db.session.commit()
#     '''
#
#     from werkzeug.security import generate_password_hash
#
#     admin = Admin(
#         name='dingweiqi1',
#         pwd=generate_password_hash('dingweiqi1'),
#         is_super=0,
#         role_id=1
#     )
#
#     db.session.add(admin)
#     db.session.commit()

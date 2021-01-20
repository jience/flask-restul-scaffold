#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

from flask_script import Manager
from flask_migrate import MigrateCommand

from app import create_app
# 使用 db migrate 命令时需要先引入所有数据库模型
from app.models import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
print(app.url_map)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# 自定义脚本命令
@manager.command
def hello():
    print('Hello')


@manager.command
def init_db():
    # todo: 完成数据初始化工作
    with app.app_context():
        # db = get_db()
        with app.open_resource('../flasky_dev.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@manager.command
def setup_db():
    # 使用 create_all 之前需要先引入所有数据库模型
    db.create_all()

    admin = User()
    admin.username = "admin",
    admin.email = "admin@example.com"
    db.session.add(admin)

    category = Category()
    category.name = 'IT'
    db.session.add(category)

    post = Post()
    post.title = 'Python'
    post.body = 'Hello Python'
    post.user = admin
    post.category = category
    db.session.add(post)

    db.session.commit()


@manager.command
def run_fake():
    from app import fake
    fake.users()
    fake.posts()


if __name__ == '__main__':
    manager.run()

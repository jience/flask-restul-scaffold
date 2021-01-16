#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

from flask_script import Manager
from flask_migrate import MigrateCommand

from app import create_app
# 需要将数据库模型导入，使用db migrate 命令时才能生效
from app.models import *

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# 自定义脚本命令
@manager.command
def hello():
    print('Hello')


@manager.command
def init_db():
    pass


if __name__ == '__main__':
    manager.run()

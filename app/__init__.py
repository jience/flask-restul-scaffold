from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.config import config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    # FlaskMigrate默认对字段属性的变动是不做检查的,所以需要添加如下配置项参数
    migrate.init_app(app, db, compare_type=True, compare_server_default=True)

    return app

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

model = SQLAlchemy()
migrate = Migrate()


# 懒加载
def init_ext(app):
    model.init_app(app)
    migrate.init_app(app=app, db=model)

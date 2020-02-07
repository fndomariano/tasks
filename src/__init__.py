from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@172.17.0.1:3306/application"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
db.create_all()

migrate = Migrate(app, db)

print(os.getenv('MYSQL_USER'))

from src.api.views.task import TaskView
from src.api.models.task import Task
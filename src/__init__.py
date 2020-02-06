from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, Manager

import os

app = Flask(__name__)

from src.api.views.task import TaskView
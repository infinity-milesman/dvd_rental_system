from flask import Blueprint

film_bp = Blueprint('film_bp',__name__)

from . import views
from . import models
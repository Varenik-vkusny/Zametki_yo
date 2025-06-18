from flask import Blueprint

addition_bp = Blueprint("addition_bp", __name__, template_folder='templates')

from . import routes
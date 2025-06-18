from flask import Blueprint

zametki_bp = Blueprint("zametki_bp", __name__, template_folder='templates')

from . import routes
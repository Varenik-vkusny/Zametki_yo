from flask import Blueprint

main_bp = Blueprint("main_bp", __name__, template_folder="templates")

from . import routes
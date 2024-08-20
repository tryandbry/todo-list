from flask import Blueprint
from . import routes  # noqa: F401


bp = Blueprint('list', __name__, template_folder='templates')

from flask import Blueprint
from .service import get_message

projects_bp = Blueprint('projects', __name__, url_prefix='/')

@projects_bp.route('/')
def index():
    message = get_message()
    return message
from flask import Blueprint, send_from_directory

static_bp: Blueprint = Blueprint('static', __name__)

@static_bp.get('/<path:path>')
def send_report(path):
    return send_from_directory('../../static/dist', path)

from flask import Blueprint, request
from flask_inertia import render_inertia
from operator import itemgetter

auth_bp: Blueprint = Blueprint('auth', __name__)

@auth_bp.route('/register')
def register():
    return render_inertia(component_name="auth/Register")

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    data = {
        "errors": {},
    }

    if request.method == 'POST':
        email, password = itemgetter('email', 'password')(request.json)
        data['errors'] = {'email': 'Error en el email'}
    return render_inertia(component_name="auth/Login", props=data)


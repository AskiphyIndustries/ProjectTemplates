from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('lolofest_applications.html')
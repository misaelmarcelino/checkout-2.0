from flask import Blueprint, render_template, request
from .ssh_service import execute_ssh

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        host = request.form.get('host')
        username = request.form.get('username')
        password = request.form.get('password')
        command = request.form.get('command')
        result = execute_ssh(host, username, password, command)
    return render_template('index.html', result=result)
        

@main.route('/checkout')
def checkout():
    return render_template('checkout.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
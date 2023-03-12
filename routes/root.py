from flask import Blueprint, render_template, send_file, redirect
root = Blueprint('root', __name__)

@root.get('/')
def home():
    return render_template('index.html')

@root.get('/socials')
def socials():
    return render_template('socials.html')

@root.get('/admin-panel')
def adminpanel():
    return render_template('adminpanel.html')#redirect("https://www.youtube.com/watch?v=p7YXXieghtost")

@root.get('/pgp.txt')
def pgp():
    return send_file('../pgp.txt')

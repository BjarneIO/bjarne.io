import re, qrcode
from flask import Blueprint, render_template, redirect, request, session, url_for

from modules.db import validate_qr_code, get_qr_url, add_qr

qr = Blueprint('qr', __name__)

@qr.get('/', defaults={'code': None})
@qr.get('/<code>')
def loadqr(code: str):

    if not 'logged_in' in session and code is None:
        return redirect(url_for('auth.auth', next=request.path))
    
    if not validate_qr_code(code):
        return render_template('qr.html')

    redirect_url = get_qr_url(code)
    return redirect(redirect_url)


@qr.post('/')
def addqr():

    url = request.form.get('url', '')
    
    if url == '':
        return render_template('qr.html')
    
    if not re.match(r'^https?://', url):
        url = 'https://' + url

    url_code = add_qr(url)
    
    img = qrcode.make(f'https://bjarne.io/qr/{url_code}')
    img.save(f'./static/codes/{url_code}.png')

    return render_template('qr.html', code=url_code)

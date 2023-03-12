from flask import Flask

from routes.root import root
from routes.qr import qr
from routes.amber import amber_route
from routes.auth import auth_route

app = Flask(__name__, template_folder='./templates', static_folder='./static')

app.config['SECRET_KEY'] = 'Sd1gr/ezf15*dz'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 3600

app.register_blueprint(root, url_prefix='/')
app.register_blueprint(qr, url_prefix='/qr')
app.register_blueprint(amber_route, url_prefix='/amber')
app.register_blueprint(auth_route, url_prefix='/auth')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1562, debug=True)

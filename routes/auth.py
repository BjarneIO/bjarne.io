
import re
from flask import Blueprint, render_template, request, redirect, url_for, session

auth_route = Blueprint('auth', __name__)

AUTH_PASS = 'Oostende'

@auth_route.route('/', methods=['GET', 'POST'])
def auth():
    next_url = request.form.get('next', request.args.get('next', None))

    if not next_url:
        return redirect(url_for('root.home'))

    # If the next URL is not a valid URL, redirect to home page
    if not re.match(r'^\/[a-zA-Z0-9?=_&\-\/]+$', next_url):
        return redirect(url_for('root.home'))

    # Page Load
    if request.method == 'GET':
        if session.get('logged_in', False):
            return redirect(next_url)

        return render_template('pass_auth.html', next=next_url, error=request.args.get('error', None))

    # Form Submit
    if not request.method == 'POST':
        return 'Error: Invalid request method'

    # If the password is incorrect, return to the auth page with an error message
    if not request.form.get('password','') == AUTH_PASS:
        return redirect(url_for('auth.auth', next=next_url, error='Incorrect password'))

    # Set logged_in to True
    session['logged_in'] = True

    return redirect(next_url)
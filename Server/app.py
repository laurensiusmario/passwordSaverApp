import os
import base64
from io import BytesIO
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session, \
    abort, jsonify, make_response, send_from_directory, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, \
    current_user
from flask_bootstrap import Bootstrap
from flask_bootstrap import WebCDN
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length, EqualTo
import onetimepass
import pyqrcode

# create application instance
app = Flask(__name__)
app.config.from_object('config')


# initialize extensions
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
lm = LoginManager(app)

app.extensions['bootstrap']['cdns']['jquery'] = WebCDN('//cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/')

# Create user class
class User(UserMixin, db.Model):
    """User model."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))
    otp_secret = db.Column(db.String(16))
    storage = db.Column(db.LargeBinary)


    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.otp_secret is None:
            # generate a random secret
            self.otp_secret = base64.b32encode(os.urandom(10)).decode('utf-8')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_totp_uri(self):
        return 'otpauth://totp/2FA-Demo:{0}?secret={1}&issuer=2FA-Demo' \
            .format(self.username, self.otp_secret)

    def verify_totp(self, token):
        return onetimepass.valid_totp(token, self.otp_secret)


@lm.user_loader
def load_user(user_id):
    """User loader callback for Flask-Login."""
    return User.query.get(int(user_id))

class RegisterForm(FlaskForm):
    """Registration form."""
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    password_again = PasswordField('Password again',
                                   validators=[Required(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """Login form."""
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    token = StringField('Token', validators=[Required(), Length(6, 6)])
    submit = SubmitField('Login')

###############################################################
#DESKTOP APP

# API untuk login.
@app.route('/api/user_login', methods=['POST'])
def user_login():

    # Receive JSON object
    name = request.json['name']
    password_input = request.json['password']
    input_token = request.json['token']

    # Username validation
    user = User.query.filter_by(username=name).first()
    if user is None or not user.verify_password(password=password_input) or not user.verify_totp(token=input_token):
        return "Invalid"
    else:
        # Valid, user log in
        login_user(user)
        return "Valid"

# API  untuk register new account
@app.route('/api/add_user', methods=['POST'])
def add_user():

    # Receive JSON object
    name = request.json['name']
    password_input = request.json['password']

    # Username validation
    user = User.query.filter_by(username=name).first()
    if user is not None:
        return "User existed"
    else:
        # Create new account
        user = User(username=name, password=password_input)
        db.session.add(user)

        db.session.commit()
        session['username'] = user.username

        return user.otp_secret

#API untuk get user.storage dari current_user
@app.route('/api/get_user_storage/', methods=['GET'])
def get_user():
    # Active user validation using cookies
    if current_user.is_authenticated:
        # Return data
        return current_user.storage.decode()
    else:
        return "get_storage not allowed"

#API untuk update storage current_user
@app.route('/api/update_user_storage/', methods=['PUT'])
def update_user_storage():
    
    # Receive JSON object
    storage_input = request.json['storage']

    # Active user validation using cookies
    if current_user.is_authenticated:
        # Update storage
        current_user.storage = storage_input.encode()
        db.session.commit()

        return "update_storage success"
    else:
        return"update_storage not allowed"

#API untuk update profil user
@app.route('/api/update_user_account/', methods=['PUT'])
def update_user_account():
    # Receive JSON object
    name = request.json['name']
    password_input = request.json['password']

    # Active user validation using cookies
    if current_user.is_authenticated:

        # Update user profile
        if (name != "") and (password_input !=""):
            # Validation using username
            user = User.query.filter_by(username=name).first()
            if user is not None:
                message="Username has been used, input another username"
            else:
                current_user.username = name
                current_user.password_hash = generate_password_hash(password_input)
                message="Username and pass changed"               
        elif (name != "") and (password_input == ""):
            # Validation using username
            user = User.query.filter_by(username=name).first()
            if user is not None:
                message="Username has been used, input another username"
            else:
                current_user.username = name
                message="Username changed"
        elif (name == "") and (password_input != ""):
            current_user.password_hash = generate_password_hash(password_input)
            message="Pass changed"

        db.session.commit()
        return message
    else:
        return "update_account not allowed"

#API untuk delete profile current_user
@app.route('/api/delete_user/', methods=['DELETE'])
def delete_user():
    # Active user validation using cookies
    if current_user.is_authenticated:
        # Delete user account
        db.session.delete(current_user)
        db.session.commit()

        return "{} account has been deleted!".format(current_user.username)
    else:
        return "delete_account not allowed"

#API untuk log out
@app.route('/api/user_logout/', methods=['GET'])
def user_logout():
    # Active user validation using cookies
    if current_user.is_authenticated:
        user=current_user.username
        logout_user()
        return "User : {}, logged out".format(user)
    else:
        return "user_logout not allowed"

###############################################################
#WEB CLIENT

@app.route('/')
def index():
    #print(session['username'])
    return render_template('index.html')

@app.route('/show', methods=['GET', 'POST'])
def show():
    if current_user.is_authenticated:
        return render_template('display.html')
    else:
        return redirect(url_for('index'))

@app.route('/store', methods=['GET', 'POST'])
def store():
    if current_user.is_authenticated:
        return render_template('store.html')
    else:
        return redirect(url_for('index'))

@app.route('/retrieve', methods=['GET'])
def retrieve():
    if current_user.is_authenticated:
        if current_user.storage is None:
            return ('',204)
        else:
            return current_user.storage.decode()
    else:
        return redirect(url_for('index'))


@app.route('/update', methods=['POST'])
def update():
    if current_user.is_authenticated:
        #print(request.form.to_dict()['data'])
        current_user.storage=request.form.to_dict()['data'].encode()
        db.session.commit()
        return ('',200)
    else:
        return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    if current_user.is_authenticated:
        # if user is logged in we get out of here
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            flash('Username already exists.')
            return redirect(url_for('register'))
        # add new user to the database
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        # redirect to the two-factor auth page, passing username in session
        session['username'] = user.username
        return redirect(url_for('two_factor_setup'))
    return render_template('register.html', form=form)


@app.route('/twofactor')
def two_factor_setup():
    if 'username' not in session:
        return redirect(url_for('index'))
    user = User.query.filter_by(username=session['username']).first()
    if user is None:
        return redirect(url_for('index'))
    # since this page contains the sensitive qrcode, make sure the browser
    # does not cache it
    return render_template('two-factor-setup.html'), 200, {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'}


@app.route('/qrcode')
def qrcode():
    if 'username' not in session:
        abort(404)
    user = User.query.filter_by(username=session['username']).first()
    if user is None:
        abort(404)

    # for added security, remove username from session
    del session['username']

    # render qrcode for FreeTOTP
    url = pyqrcode.create(user.get_totp_uri())
    stream = BytesIO()
    url.svg(stream, scale=3)
    return stream.getvalue(), 200, {
        'Content-Type': 'image/svg+xml',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'}


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route."""
    if current_user.is_authenticated:
        # if user is logged in we get out of here
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data) or \
                not user.verify_totp(form.token.data):
            flash('Invalid username, password or token.')
            return redirect(url_for('login'))

        # log user in
        login_user(user)
        flash('You are now logged in!')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """User logout route."""
    logout_user()
    return redirect(url_for('index'))


@app.route('/offline.html')
def offline():
    return app.send_static_file('offline.html')


@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

# create database tables if they don't exist yet
db.create_all()


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, ssl_context='adhoc')

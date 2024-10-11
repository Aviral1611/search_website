from flask import Flask, request, render_template
from exa_py import Exa
import os
from dotenv import load_dotenv
from flask import  redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


load_dotenv()



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
exa = Exa(api_key=os.getenv("EXA_API_KEY"))


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "info"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if the username already exists
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))

        # Add the new user to the database
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form,title="Register")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:  # Compare hashed passwords in production
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))

        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form,title="Login")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        selected_domains = request.form.getlist('domains')  # Retrieve selected domains from the form
        
        # Perform the search using the selected domains
        response = exa.search(
            query,
            num_results=10,
            type='keyword',
            include_domains=selected_domains,  # Use selected domains
        )
        results = response.results
    else:
        query = None
        results = []
    return render_template('index.html', query=query, results=results,title="Home")

if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Justyna R',
        'title': 'Bloody Moon',
        'content': 'I didn\'t saw blood moon',
        'date_posted': 'July 27, 2018'
    },
    {
        'author': 'Darek R',
        'title': 'Starcraft rules',
        'content': 'On the first day of christmas blizzard gave to me',
        'date_posted': 'July 27, 2018'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'aaa@gmail.com' and form.password.data == 'pass':
            flash('You have been loged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0956216755cc68d17ee4ee8862451d93'


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
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
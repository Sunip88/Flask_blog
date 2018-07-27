from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
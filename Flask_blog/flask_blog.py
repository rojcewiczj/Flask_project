
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']='WhereIsTheHorseAndTheRider'
posts = [
    {
        'author': "John Rojcewicz",
        'title': "Blog Post 1",
        'content': 'First post content',
        'date_posted': 'April 21, 2018'
    },
     {
        'author': "John Rojcewicz",
        'title': "Blog Post 2",
        'content': 'second post content',
        'date_posted': 'March 3rd, 2018'
    }
]

@app.route("/")
def hello():
    return "<h1>Hello World</h1>"

@app.route("/home")
def Home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title = 'About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators

DEBUG = False

# ReCaptcha
# Keys for localhost

app = Flask(__name__, template_folder='templates')
app.config.from_object(__name__)

app.secret_key = 'YourSuperSecreteKey'


@app.route('/', methods=('GET', 'POST'))
def home():
    return render_template('index.html/')


@app.route('/welcome', methods=('GET', 'POST'))
def welcome():
    return render_template('welcome.html/')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    return render_template('contact.html/')


@app.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('about.html/')


@app.route('/resume', methods=('GET', 'POST'))
def resume():
    return render_template('resume.html/')


@app.route('/datascience', methods=('GET', 'POST'))
def datascience():
    return render_template('datascience.html/')


@app.route('/articles', methods=('GET', 'POST'))
def articles():
    return render_template('articles.html/')


@app.route('/business', methods=('GET', 'POST'))
def business():
    return render_template('business.html/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG, port=5001)

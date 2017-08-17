from datetime import datetime
from flask import Flask, render_template
from flask import request
from flask import make_response
from flask import redirect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
#from flask.ext.bootstrap import Bootstrap
#from flask.ext.moment import Moment
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    #    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/redirect')
def redi():
    return redirect('https://www.baidu.com')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)

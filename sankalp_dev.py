from flask import Flask,render_template
import simplejson as json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


with open('config-home.json','r') as c:
   params = json.load(c)["params"]


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/sankalpdev'
db = SQLAlchemy(app)


class Posts(db.Model):
    srn = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    catogary = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(50), nullable=True)
    content = db.Column(db.String(300), nullable=False)
    img_file = db.Column(db.String(50), nullable=True)

@app.route('/')
def home():
    posts = Posts.query.filter_by().all()[0:params['no_of_posts']]
    return render_template('index.html',params=params,posts=posts)

@app.route('/blog')
def blog():
    pass

@app.route('/paths')
def paths():
    pass

@app.route('/about')
def about():
    pass

@app.route('/contect')
def contect():
    pass

@app.route('/privacy')
def privacy():
    pass
@app.route('/sitemap')
def sitemap():
    pass



app.run(debug=True)
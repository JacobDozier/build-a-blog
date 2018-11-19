from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = '%9VK@b2Bt^gu'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(255))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/newpost', methods=['POST'])
def new_post():
    return redirect('/blog')
    
@app.route('/', methods=['POST', 'GET'])
def index():

    blog_posts = Blog.query.all()
    return render_template('posts.html', page_title="Build a Blog", blog_posts=blog_posts)


if __name__ == '__main__':
    app.run()
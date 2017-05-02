# https://stackoverflow.com/questions/40943625/connect-to-mysql-with-sqlalchemy-and-query/40944291#40944291

from flask import Flask, request, url_for, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:chitts@localhost/myscratchpad'

db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", comments=Comments.query.all())

    entry = Comments(id=request.form["id"], content=request.form["contents"])
    db.session.add(entry)
    db.session.commit()


    return redirect(url_for('index'))

class Comments(db.Model):
	__tablename__ = 'comments'
	id = db.Column('id', db.Integer, primary_key=True)
	content = db.Column('content', db.Unicode)

	def __init__(self, id, content):
		self.id = id
		self.content = content


if __name__ == '__main__':
	app.run(debug=True)
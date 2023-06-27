from flask import Flask ,render_template ,request ,redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy

#Init
db_name = 'spisak.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
#Content
class Spisak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128),nullable=False)

    def __repr__(self):
        return str(self.content)

@app.route('/',methods=['POST','GET'])

def index():
    spisak = Spisak.query.all()
    return render_template('index.html',contents=spisak)

@app.route('/add' , methods=['POST'])
def add():
    new_content = Spisak(content=request.form['content'])
    db.session.add(new_content)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    content = Spisak.query.get(id)
    db.session.delete(content)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
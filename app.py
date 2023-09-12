from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To prevent warning message

app.secret_key = 'mysecret' # Add a secret key for session management
db = SQLAlchemy(app)

# pylint: disable=no-member
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
# pylint: enable=no-member

    def __repr__(self):
        return f"User('{self.username}')"

# Initialize Flask-Admin and add the User model to the admin interface
admin = Admin(app)
admin.add_view(ModelView(User, db.session))

@app.route('/')
def index():
    return render_template("/home.html")

@app.route('/add_user/<username>')
def add_user(username):
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return f"Added user: {username}"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

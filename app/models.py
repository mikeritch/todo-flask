import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login



class User(UserMixin, db.Model):
    """This Schema defines the Users table and stores their data"""

    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("Username", db.String(64), index=True, unique=True)
    email = db.Column("Email", db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    todos = db.relationship('Todo', backref="author", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Todo(db.Model):
    """This Schema defines the Todo table and stores the list data"""

    todo_id = db.Column("todo_id", db.Integer, primary_key=True)
    title = db.Column("Title", db.String(40), nullable=False)
    description = db.Column("Description", db.String(244), default="")
    created_on = db.Column("CreatedOn", db.DateTime, index=True, default=datetime.datetime.utcnow)
    _is_done = db.Column("_is_done", db.Boolean, default=False)
    _is_deleted = db.Column("_is_deleted", db.Boolean, default=False)
    created_by = db.Column("CreatedBy", db.String(64), db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Todo {self.title}"

    def add_todo(self):
        db.session.add(self)
        return db.session.commit()
    
    def delete_todo(todo_id):
        Todo.query.filter_by(todo_id=todo_id).update({"_is_deleted" : True})
        print(f"Attempting to delete {todo_id}")
        return db.session.commit()

    def recycle():
        recycling = Todo.query.filter_by(_is_deleted=True).all()
        for i in recycling:
            db.session.delete(i)
        return db.session.commit()
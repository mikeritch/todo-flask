from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user

from app import app
from app.forms import LoginForm, AddItemForm
from app.models import User, Todo

@app.route("/")
@app.route("/index")
def index():
    """Main page for todo list"""
    add = AddItemForm()
    todos = Todo.fetch_all()
    return render_template("index.html", title= 'To Do List', form=add, todos=todos, update=update)

@app.route("/add", methods=["POST"])
def add():
    """ADD ITEM: HTTP Post request to add todo item to db"""
    add = AddItemForm()
    new = Todo(title=add.title.data, description=add.description.data)
    Todo.add_todo(new)
    return redirect(url_for("index", _anchor="title"))

@app.route("/update/<todo_id>", methods=["GET", "PUT", "POST"])
def update(todo_id):
    update = todo_id
    return redirect(url_for("index", _anchor="", update=update))

@app.route("/delete/<todo_id>", methods=["GET", "POST"])
def delete(todo_id):
    """DELETE ITEM: Marking todo item for deletion. Does not carry out database query"""
    Todo.delete_todo(todo_id)
    return redirect(url_for("index", _anchor="todolist_wrapper"))

@app.route("/recycle")
def recycle():
    """DB CLEANUP: Carries out database garbage collection, drops instances in db marked for deletion"""
    Todo.recycle()
    return redirect(url_for("index"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """Logs user into session"""
    if current_user.is_authenticated:
        flash("You're already logged in")
        return redirect(url_for("index"))
    pageform = LoginForm()
    if pageform.validate_on_submit():
        user = User.query.filter_by(username=pageform.username.data).first()
        if user is None or not user.check_password(pageform.password.data):
            flash("Invalid Username or password", category="error")
            return redirect(url_for("login"))
        login_user(user, remember=pageform.remember_me.data)
        flash(f"Login requested for user {pageform.username.data}, remember_me = {pageform.remember_me.data}")
        return redirect(url_for("index"))
    return render_template("login.html", title='Sign In', form=pageform)

@app.route("/logout")
def logout():
    """Logs user out of session"""
    logout_user()
    return redirect(url_for("index"))
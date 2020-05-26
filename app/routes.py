from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user

from app import app
from app.forms import LoginForm, AddItemForm
from app.models import User, Todo

@app.route("/")
@app.route("/index")
def index():
    add = AddItemForm()
    todos = Todo.query.filter_by(_is_deleted=False).all()
    return render_template("index.html", title= 'To Do List', form=add, todos=todos)

@app.route("/add", methods=["POST"])
def add():
    add = AddItemForm()
    new = Todo(title=add.title.data)
    Todo.add_todo(new)
    return redirect(url_for("index"))

@app.route("/delete/<todo_id>", methods=["GET", "POST"])
def delete(todo_id):
    Todo.delete_todo(todo_id)
    return redirect(url_for("index"))

@app.route("/recycle")
def recycle():
    Todo.recycle()
    return redirect(url_for("index"))

@app.route("/login", methods=["GET", "POST"])
def login():
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
    logout_user()
    return redirect(url_for("index"))
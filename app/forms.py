from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")

class AddItemForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Describe your To Do")
    due_date = DateField(label="dd-mm-yy", format="%d-%m-%y")
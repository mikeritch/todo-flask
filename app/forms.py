from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Sign In")

class AddItemForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired(), Length(max=40)], )
    description = StringField(label="Description")
    #due_date = DateField(label="Due Date")
    add_button = SubmitField(label="")
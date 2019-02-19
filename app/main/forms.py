from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from ..models import User

class AddAuthor(FlaskForm):
	author = StringField('author name',validators=[Required()])

class BlogForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    description = TextAreaField('description',validators = [Required()])
    submit = SubmitField('Submit')






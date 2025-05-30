
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, FileField
from wtforms.validators import DataRequired



class BookForm(FlaskForm):
    title = StringField("Название книги", validators=[DataRequired()])
    author = SelectField("Автор", coerce=int, validators=[DataRequired()])
    genres = SelectMultipleField("Жанры", coerce=int, validators=[DataRequired()])
    cover = FileField("Обложка")
    submit = SubmitField("Сохранить")

class AuthorForm(FlaskForm):
    name = StringField("Имя автора", validators=[DataRequired()])
    submit = SubmitField("Сохранить")

class GenreForm(FlaskForm):
    name = StringField("Название жанра", validators=[DataRequired()])
    submit = SubmitField("Сохранить")

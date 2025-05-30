from . import db
from flask_login import UserMixin

# Связующая таблица книга-жанр
book_genre = db.Table('book_genre',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)

# Книга
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)  # Описание книги
    analysis_result = db.Column(db.Text)  # Результат AI-анализа
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    genres = db.relationship('Genre', secondary=book_genre, backref='books')
    cover = db.Column(db.String(100))  # Путь к изображению

# Автор
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    books = db.relationship('Book', backref='author')

# Жанр
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

# Пользователь
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

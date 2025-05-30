import os
from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from werkzeug.utils import secure_filename
from flask_login import login_required
from . import db
from .models import Book, Author, Genre
from .forms import BookForm, AuthorForm, GenreForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    query = request.args.get('q')
    books = Book.query

    if query:
        books = books.join(Author).filter(
            (Book.title.ilike(f'%{query}%')) |
            (Author.name.ilike(f'%{query}%'))
        )

    books = books.all()
    return render_template('index.html', books=books)


@main.route('/authors')
def authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)


@main.route('/genres')
def genres():
    genres = Genre.query.all()
    return render_template('genres.html', genres=genres)


@main.route('/book/add', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    form.author.choices = [(a.id, a.name) for a in Author.query.all()]
    form.genres.choices = [(g.id, g.name) for g in Genre.query.all()]

    if form.validate_on_submit():
        filename = None
        if form.cover.data:
            filename = secure_filename(form.cover.data.filename)

            # Путь к папке uploads внутри static
            upload_folder = os.path.join(current_app.root_path, 'static/uploads')
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            path = os.path.join(upload_folder, filename)
            form.cover.data.save(path)

        book = Book(
            title=form.title.data,
            author_id=form.author.data,
            cover=filename
        )
        for genre_id in form.genres.data:
            genre = Genre.query.get(genre_id)
            book.genres.append(genre)
        db.session.add(book)
        db.session.commit()
        flash("Книга добавлена!")
        return redirect(url_for('main.index'))

    return render_template('book_form.html', form=form)


@main.route('/book/edit/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    form = BookForm(obj=book)

    form.author.choices = [(a.id, a.name) for a in Author.query.all()]
    form.genres.choices = [(g.id, g.name) for g in Genre.query.all()]
    form.genres.data = [g.id for g in book.genres]

    if form.validate_on_submit():
        book.title = form.title.data
        book.author_id = form.author.data

        if form.cover.data:
            filename = secure_filename(form.cover.data.filename)

            upload_folder = os.path.join(current_app.root_path, 'static/uploads')
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            path = os.path.join(upload_folder, filename)
            form.cover.data.save(path)
            book.cover = filename

        book.genres = []
        for genre_id in form.genres.data:
            genre = Genre.query.get(genre_id)
            book.genres.append(genre)

        db.session.commit()
        flash("Книга обновлена!")
        return redirect(url_for('main.index'))

    return render_template('book_form.html', form=form)


@main.route('/book/delete/<int:book_id>', methods=['POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash("Книга удалена!")
    return redirect(url_for('main.index'))


@main.route('/author/add', methods=['GET', 'POST'])
@login_required
def add_author():
    form = AuthorForm()
    if form.validate_on_submit():
        author = Author(name=form.name.data)
        db.session.add(author)
        db.session.commit()
        flash("Автор добавлен!")
        return redirect(url_for('main.index'))
    return render_template('author_form.html', form=form)


@main.route('/author/edit/<int:author_id>', methods=['GET', 'POST'])
@login_required
def edit_author(author_id):
    author = Author.query.get_or_404(author_id)
    form = AuthorForm(obj=author)
    if form.validate_on_submit():
        author.name = form.name.data
        db.session.commit()
        flash("Автор обновлён!")
        return redirect(url_for('main.index'))
    return render_template('author_form.html', form=form)


@main.route('/author/delete/<int:author_id>', methods=['POST'])
@login_required
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    flash("Автор удалён!")
    return redirect(url_for('main.index'))


@main.route('/genre/add', methods=['GET', 'POST'])
@login_required
def add_genre():
    form = GenreForm()
    if form.validate_on_submit():
        genre = Genre(name=form.name.data)
        db.session.add(genre)
        db.session.commit()
        flash("Жанр добавлен!")
        return redirect(url_for('main.index'))
    return render_template('genre_form.html', form=form)


@main.route('/genre/edit/<int:genre_id>', methods=['GET', 'POST'])
@login_required
def edit_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    form = GenreForm(obj=genre)
    if form.validate_on_submit():
        genre.name = form.name.data
        db.session.commit()
        flash("Жанр обновлён!")
        return redirect(url_for('main.index'))
    return render_template('genre_form.html', form=form)


@main.route('/genre/delete/<int:genre_id>', methods=['POST'])
@login_required
def delete_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    db.session.delete(genre)
    db.session.commit()
    flash("Жанр удалён!")
    return redirect(url_for('main.index'))

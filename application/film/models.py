from .. import db

from sqlalchemy.dialects.postgresql import TSVECTOR

class Film(db.Model):
    __tablename__ = 'film'

    id = db.Column('film_id',db.Integer, primary_key=True, nullable=False)
    title = db.Column('title',db.String(256), nullable=False)
    description = db.Column(db.Text)
    release_year = db.Column(db.Integer)
    language_id = db.Column(db.SmallInteger, nullable=False)
    rental_duration = db.Column(db.SmallInteger, nullable=False)
    rental_rate = db.Column(db.Numeric(4,2), nullable=False)
    length = db.Column(db.SmallInteger)
    replacement_cost = db.Column(db.Numeric(5,2), nullable=False)
    rating = db.Column(db.String(256))
    special_features = db.Column(db.ARRAY(db.Text()))
    fulltext = db.Column(TSVECTOR, nullable=False, index=True)
    create_dttm = db.Column(db.DateTime)
    update_dttm = db.Column(db.DateTime)


    def __repr__(self):
        return f"<Film>:{self.id}, <title>:{self.title}"

class FilmCategory(db.Model):
    __tablename__ = 'film_category'

    film_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, nullable=False)
    create_dttm = db.Column(db.DateTime)
    update_dttm = db.Column(db.DateTime)

    def __repr__(self):
        return f"<FilmCategory>:{self.film_id}>"

class Category(db.Model):
    ___tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    create_dttm = db.Column(db.DateTime)
    update_dttm = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Category>:{self.category_id}>"

class Language(db.Model):
    __tablename__ = 'language'

    language_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    create_dttm = db.Column(db.DateTime)
    update_dttm = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Language>:{self.language_id}>"

class FilmActor(db.Model):
    __tablename__ = 'film_actor'

    actor_id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, nullable=False)
    create_dttm = db.Column(db.DateTime)
    update_dttm = db.Column(db.DateTime)

    def __repr__(self):
        return f"<FilmActor>:{self.actor_id}>"






















from .. import db

class Film(db.Model):
    __table_name__ = 'film'

    id = db.Column('film_id',db.Integer, primary_key=True)
    title = db.Column('title',db.String(256))
    description = db.Column('description',db.String(256))
    release_year = db.Column(db.Integer)
    language_id = db.Column(db.Integer)
    rental_duration = db.Column(db.String(256))
    rental_rate = db.Column(db.Float)
    length = db.Column(db.String(256))
    replacement_cost = db.Column(db.Float)
    rating = db.Column(db.Float)
    special_features = db.Column(db.String(256))
    fulltext = db.Column(db.String(256))
    create_dttm = db.Column(db.String(256))
    update_dttm = db.Column(db.String(256))


    def __repr__(self):
        return f"<id>:{self.id}, <title>:{self.title}"
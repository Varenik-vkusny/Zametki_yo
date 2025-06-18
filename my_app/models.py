from my_app import db

class Zametka(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Zametka {self.id}>'
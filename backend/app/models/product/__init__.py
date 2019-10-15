from app import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)
    status =  db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<%Product: {self.title} %>"
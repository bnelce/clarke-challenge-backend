from shared.database import db


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    cost_per_kwh = db.Column(db.Float, nullable=False)
    min_kwh = db.Column(db.Integer, nullable=False)
    total_clients = db.Column(db.Integer, nullable=False)
    avg_rating = db.Column(db.Float, nullable=False)

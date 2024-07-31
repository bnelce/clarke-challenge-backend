from app.shared.database import db

class Supplier(db.Model):
    __tablename__ = "suppliers"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    logo = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    cost_per_kwh = db.Column(db.Float, nullable=False)
    min_kwh = db.Column(db.Integer, nullable=False)
    total_clients = db.Column(db.Integer, nullable=False)
    average_rating = db.Column(db.Float, nullable=False)

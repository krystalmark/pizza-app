from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __init__(self, name, address):
        self.name = name
        self.address = address

class Pizza(db.Model):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    restaurant = db.relationship('Restaurant', backref=db.backref('restaurant_pizzas', lazy=True))
    pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizzas', lazy=True))

    def __init__(self, price, restaurant, pizza):
        self.price = price
        self.restaurant = restaurant
        self.pizza = pizza

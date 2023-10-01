from flask import Flask, jsonify, request
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)

# Route to get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [
        {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
        for restaurant in restaurants
    ]
    return jsonify(restaurant_list)

# Route to get a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizzas = [
            {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }
            for pizza in restaurant.pizzas
        ]
        return jsonify({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': pizzas
        })
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

# Route to delete a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        # Delete associated RestaurantPizza entries first
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

# Route to get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [
        {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }
        for pizza in pizzas
    ]
    return jsonify(pizza_list)

# Route to create a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Add validation for price here if needed

    restaurant_pizza = RestaurantPizza(
        price=price,
        pizza_id=pizza_id,
        restaurant_id=restaurant_id
    )
    db.session.add(restaurant_pizza)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)

    return jsonify({
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    }), 201

if __name__ == '__main__':
    app.run(debug=True)

from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    restaurant1 = Restaurant(name='Sarova', address='Hilton,Nairobi')
    restaurant2 = Restaurant(name='Red Ginger', address='Parklands,Nairobi')
    restaurant3 = Restaurant(name='Moha', address='Eastleigh,Nairobi')
    restaurant4 = Restaurant(name='The Ark', address='Nyeri')
    restaurant5 = Restaurant(name='Kilele', address='Parklands,Nairobi')
    restaurant6 = Restaurant(name='CJ', address='Westlands,Nairobi')
    
    pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
    pizza3 = Pizza(name='Borewores', ingredients='Dough, Tomato Sauce, Cheese,Ham')
    pizza4 = Pizza(name='Hawaiian', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni,Pineapple')
    pizza5 = Pizza(name='Meat Deluxe', ingredients='Dough, Tomato Sauce, Cheese,Meat')
    pizza6 = Pizza(name='Veg', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni,Mushroom')
    db.session.add_all([restaurant1, restaurant2,restaurant3,restaurant4,restaurant5,restaurant6, pizza1, pizza2,pizza3,pizza4,pizza5,pizza6])
    db.session.commit()

    association1 = RestaurantPizza(price=10, pizza=pizza1, restaurant=restaurant1)
    association2 = RestaurantPizza(price=12, pizza=pizza2, restaurant=restaurant1)
    association3 = RestaurantPizza(price=9, pizza=pizza1, restaurant=restaurant2)
    association4 = RestaurantPizza(price=7.5, pizza=pizza1, restaurant=restaurant1)
    association5 = RestaurantPizza(price=13, pizza=pizza2, restaurant=restaurant1)
    association6 = RestaurantPizza(price=8.5, pizza=pizza1, restaurant=restaurant2)

    db.session.add_all([association1, association2, association3,association4,association5,association6])
    db.session.commit()

print("Database seeded successfully.")

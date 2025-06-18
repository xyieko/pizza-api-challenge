import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    
    pepperoni = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    hawaiian = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Ham, Pineapple")
    db.session.add_all([pepperoni, hawaiian])

    
    elaines = Restaurant(name="Trish's Pizza", address="15 Langata, Nairobi")
    mama_roma = Restaurant(name="Mama Chira", address="45 Moi Avenue, Nairobi")
    db.session.add_all([elaines, mama_roma])

    db.session.commit()

    
    rp1 = RestaurantPizza(price=15, pizza_id=pepperoni.id, restaurant_id=elaines.id)
    rp2 = RestaurantPizza(price=18, pizza_id=hawaiian.id, restaurant_id=mama_roma.id)
    db.session.add_all([rp1, rp2])

    db.session.commit()

    

# 🍕 Pizza Restaurant API

A RESTful API built with Flask to manage pizzas, restaurants, and their prices. No frontend required — test using Postman or cURL.

## 🔧 Tech Stack
- Python + Flask
- Flask SQLAlchemy
- SQLite (local dev)

## 🧩 Models
- **Pizza**: `id`, `name`, `ingredients`
- **Restaurant**: `id`, `name`, `address`
- **RestaurantPizza**: `id`, `price`, `pizza_id`, `restaurant_id`

> `price` must be between 1 and 30.

## 🚀 Endpoints

### `GET /pizzas`
Returns all pizzas.

### `GET /restaurants`
Returns all restaurants.

### `GET /restaurants/<id>`
Returns a restaurant with its pizzas and prices.

### `POST /restaurant_pizzas`
Adds a pizza to a restaurant.


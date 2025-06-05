from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# الاتصال بقاعدة البيانات (Atlas أو محلي)
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://Store:ihge2660@mystoreproject.udmwjft.mongodb.net/store?retryWrites=true&w=majority")
client = MongoClient(MONGO_URI)
db = client["store"]
collection = db["products"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/api/products', methods=['GET'])
def get_products():
    products = list(collection.find({}, {"_id": 0}))
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    collection.insert_one(data)
    return jsonify({"msg": "تمت الإضافة"})

@app.route('/api/products', methods=['PUT'])
def update_product():
    data = request.json
    collection.update_one({"name": data['name']}, {"$set": data})
    return jsonify({"msg": "تم التحديث"})

@app.route('/api/products', methods=['DELETE'])
def delete_product():
    name = request.json['name']
    collection.delete_one({"name": name})
    return jsonify({"msg": "تم الحذف"})

if __name__ == '__main__':
    app.run(debug=True)

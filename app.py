from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# الاتصال بقاعدة البيانات عبر متغير البيئة
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["store"]  # يمكنك تغييره لاسم قاعدة البيانات الفعلي
collection = db["products"]  # مثال على مجموعة بيانات

# نقطة اختبار رئيسية
@app.route("/")
def home():
    return jsonify({"message": "API is running on Render 🎉"})

# إضافة منتج (مثال)
@app.route("/add", methods=["POST"])
def add_product():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "Missing product data"}), 400
    collection.insert_one(data)
    return jsonify({"message": "Product added successfully"}), 201

# عرض كل المنتجات (مثال)
@app.route("/products", methods=["GET"])
def get_products():
    products = list(collection.find({}, {"_id": 0}))  # تجاهل _id في الإخراج
    return jsonify(products)

# إعداد السيرفر للعمل على Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

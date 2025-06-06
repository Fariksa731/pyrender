from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# قراءة رابط الاتصال من متغير البيئة
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["store"]
products_collection = db["products"]

@app.route("/")
def index():
    products = list(products_collection.find())
    return render_template("index.html", products=products)

# مثال على صفحة اختبار
@app.route("/test-mongo")
def test_mongo():
    try:
        count = products_collection.count_documents({})
        return f"✅ MongoDB Connected. عدد المنتجات: {count}"
    except Exception as e:
        return f"❌ MongoDB Error: {e}"

# بدء التطبيق على 0.0.0.0 وليس localhost فقط
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

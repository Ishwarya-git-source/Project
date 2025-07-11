from flask import Flask

app = Flask(__name__)

@app.route("/products")
def products():
    return {"products": ["Laptop", "Phone", "Tablet", "Airpods"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

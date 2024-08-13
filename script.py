from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for processed data
processed_data_storage = {}

# Mock data for simulation
mock_data = {
    "products": [
        {"id": 1, "name": "Product A", "price": 100},
        {"id": 2, "name": "Product B", "price": 200},
        {"id": 3, "name": "Product C", "price": 300}
    ]
}

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Simulate fetching data from an external service
    return jsonify(mock_data)

@app.route('/process-data', methods=['POST'])
def process_data():
    data = request.json
    # Simple transformation: Convert all product names to uppercase
    for product in data.get('products', []):
        product['name'] = product['name'].upper()
    
    # Store processed data in memory
    processed_data_storage['products'] = data['products']
    return jsonify({"message": "Data processed and stored successfully."})

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    # Return the processed data stored in memory
    return jsonify(processed_data_storage)

if __name__ == '__main__':
    app.run(debug=True)

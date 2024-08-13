# Flask Data Retrieval and Processing Application

## Overview
This Flask application simulates a simplified version of a data retrieval and processing system. It includes the following features:
1. API Endpoint for Data Retrieval: `/fetch-data`
2. Data Processing: `/process-data`
3. Data Storage: In-memory storage (Python dictionary)
4. API Endpoint for Processed Data Retrieval: `/get-processed-data`

## Setup and Run Locally

### Prerequisites
- Python 3.x
- Flask

### Installation
1. Clone the repository:
   git clone https://github.com/HariChandana2000/Vervo-Flask-Project.git
   
3. Navigate to the project directory:
   cd Vervo-Flask-Project
   
4. pip3 install Flask
   
### Running the Application
1. Start the Flask application:
   python3 script.py

2. The application will be available at `http://127.0.0.1:5000/`.

### API Endpoints
1. **Fetch Data**
- Endpoint: `/fetch-data`
- Method: `GET`
- Description: Simulates fetching data from an external service.

2. **Process Data**
- Endpoint: `/process-data`
- Method: `POST`
- Description: Processes the fetched data (e.g., converts text to uppercase) and stores it in memory.
- Example Request Body:
  ```json
  {
    "products": [
      {"id": 1, "name": "Product A", "price": 100},
      {"id": 2, "name": "Product B", "price": 200},
      {"id": 3, "name": "Product C", "price": 300}
    ]
  }
  ```

3. **Get Processed Data**
- Endpoint: `/get-processed-data`
- Method: `GET`
- Description: Returns the processed data stored in memory.




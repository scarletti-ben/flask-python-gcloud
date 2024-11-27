from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app) # Makes the app accept cross origin api requesting

# Get environment variables
app.config["DEBUG"] = os.environ.get("FLASK_DEBUG")

# In the server create a Home route
@app.route('/')
def hello_world():
    """Function to act as an endpoint to return Hello, World! when we got to that URL"""
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
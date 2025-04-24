from flask import Flask
import requests

app = Flask(__name__)

REPLIT_URL = "https://b4dad1bb-a3bb-41e7-8dc8-f8d3d7453b8b-00-1loqz2ubw5tj3.pike.replit.dev/"

@app.route('/')
def home():
    try:
        requests.get(REPLIT_URL)
        return "Pinged your Replit bot!"
    except:
        return "Failed to ping Replit bot."

if __name__ == "__main__":
    app.run()
  

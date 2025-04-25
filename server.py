from flask import Flask
import requests

app = Flask(__name__)

REPLIT_URL = "https://2e11e93e-5882-4e5f-84a5-046cb70de076-00-156kht34tm5io.janeway.replit.dev"

@app.route('/')
def home():
    try:
        requests.get(REPLIT_URL)
        return "Pinged your Replit bot!"
    except:
        return "Failed to ping Replit bot."

if __name__ == "__main__":
    app.run()
  

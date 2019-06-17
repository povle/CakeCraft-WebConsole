#!python3.7
from app import app
import os
if __name__ == "__main__":
    if os.environ.get("FLASK_ENV") == "production":
        app.run(host="127.0.0.1", port=80) # Temporary
    else:
        app.run()

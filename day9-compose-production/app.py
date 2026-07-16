import os
import redis
from flask import Flask

app = Flask(__name__)

# Read the secret from the mounted secret file (default /run/secrets/my_secret)
secret_path = os.environ.get("SECRET_PATH", "/run/secrets/my_secret")
try:
    with open(secret_path, "r") as f:
        my_secret = f.read().strip()
except FileNotFoundError:
    my_secret = "default-secret"

# Connect to Redis using host from environment
redis_host = os.environ.get("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    count = r.incr("hits")
    return f"<h1>Production Compose Demo</h1><p>Hits: {count}</p><p>Secret says: {my_secret}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

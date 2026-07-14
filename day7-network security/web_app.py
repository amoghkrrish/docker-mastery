from flask import Flask
import os, redis

app = Flask(__name__)
redis_host = os.environ.get("REDIS_HOST","localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():
    count = r.incr("hits")
    return f"<h1>Public Web</h1><p>Hits: {count}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

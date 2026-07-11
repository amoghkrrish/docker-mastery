import os
from flask import Flask
import redis

app= Flask(__name__)

redis_host = os.environ.get("REDIS_HOST","localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route("/")
def home():

	count=r.incr("visits")
	return f"<h1>Hello from Docker Compose!</h1><p>Page visited {count} times. </p>"

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=8080)


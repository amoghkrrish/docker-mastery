import redis, time, os

redis_host = os.environ.get("REDIS_HOST","localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

while True:
     r.incr("background_jobs")
     print("Worker processed a job")
     time.sleep(5)

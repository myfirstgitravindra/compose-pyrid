from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route('/')
def hello():
    # Increment visit count
    visit_count = redis_client.incr('visits')
    return f"Hello Docker World! You've visited this page {visit_count} times."

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask
from datetime import datetime
app = Flask(__name__)



@app.route("/")
def hello():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Hello, from container! time :{time}"

if __name__ == "__main__":
    app.run()
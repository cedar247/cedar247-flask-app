from unittest import result
from flask import Flask, request
from flask_cors import CORS, cross_origin

from Scheduler import Scheduler

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/schedule', methods=['POST'])
@cross_origin()
def create_schedule():
    data = request.form.get("x")
    scheduler = Scheduler()
    result = scheduler.get_schedule()
    return result

if __name__ == "__main__":
    app.run(port=4000, debug=True)
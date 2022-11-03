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
    data = request.get_json()


    doctors_details = data["doctors_details"]
    shift_types = data["shift_types"]
    consecutive_shifts = data["consecutive_shifts"]
    special_shifts = data["special_shifts"]
    num_doctors = data["num_doctors"]
    doctor_categories = data["doctorCategories"]
    
    results = []

    for category in doctor_categories:
        scheduler = Scheduler(doctors_details[category], shift_types, special_shifts, num_doctors[category], 2022, 12)
        results.append(scheduler.get_schedule())

    return results

if __name__ == "__main__":
    app.run(port=5000, debug=True)
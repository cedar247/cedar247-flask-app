from flask import Flask

app = Flask(__name__)

@app.route('/schedule', methods=['GET'])
def create_schedule():
    return "create schedule"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
from flask import Flask,render_template
import sys
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route("/")
@cross_origin()
def index():
    print("Entering Infinite Loop", file=sys.stderr)
    while True:
        pass
    print("*******Exiting Infinite Loop********", file=sys.stderr)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

from flask import Flask, request, jsonify
from flask_cors import CORS
from topics import get_topics
from material import get_materials
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'hello hackoasis :)'


@app.route('/learn', methods=['GET', 'POST'])
def send_data():
    to_send = []
    data = request.json
    subject = data.get('subject')
    learner_type = data.get('type')
    topics = get_topics(subject)
    for topic in topics:
        to_send.append(get_materials(topic, learner_type))
    return json.dumps(to_send)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9000, debug=True)
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import re
import helpers

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=["POST"])
@cross_origin()
def analyse_text():
    text = request.json["text"].lower()

    length_with_space, length_without_space = helpers.count_text_length(text)
    data = {
        "textLength": {
            "withSpaces": length_with_space,
            "withoutSpaces": length_without_space
        },
        "wordCount": helpers.count_text_length(text),
        "characterCount": helpers.count_text_characters(text)
    }

    return data

if __name__ == "__main__":
    app.run()


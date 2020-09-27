import json


def test_analyse_text_view(app, client):
    payload = {"text":"hello 2 times  "}
    headers = {"Content-type": "application/json"}
    res = client.post("/", data=payload, headers=headers)

    assert res.status_code == 200
    expected = {
        "textLength":{"withSpaces":15,"withoutSpaces":11},
        "wordCount":3,
        "characterCount":[{"e":2},{"h":1},{"i":1},{"l":2},{"m":1},{"o":1},{"s":1},{"t":1}]
    }
    assert expected == json.loads(res.get_data(as_text=True))

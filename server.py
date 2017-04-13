from flask import Flask
from flask import request

from flask import json
import publisher

git_repo=''

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/git-updates", methods=['POST'])
def deploy_app():
    request_json=json.dumps(request.json)
    print request_json
    git_url=request_json[0];
    publisher.publish(git_url);
    return "sent-update"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

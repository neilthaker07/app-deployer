from flask import Flask
import publisher

git_repo=''

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/deploy/<name>")
def deploy_app(name):
    publisher.publish(name);
    return "sent-update";


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

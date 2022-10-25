from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/ping')
def ping():  # put application's code here
    print("ping")
    return 'up'

if __name__ == '__main__':
    app.run()

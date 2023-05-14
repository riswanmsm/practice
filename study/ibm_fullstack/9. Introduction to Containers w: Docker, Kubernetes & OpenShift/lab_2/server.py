# this is a flak server for creating API
from flask import Flask

app = Flask('Fask App')


@app.route('/')
def say_hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=8000, debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<html><head><title>Metas</title></head></html>'

if __name__ == '__main__':
    app.run(debug=True)

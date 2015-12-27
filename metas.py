from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/meta/')
@app.route('/meta/<meta>')
def metas(meta=None):
	if meta is None:
		return 'Todas as metas <list>'
	return 'Meta {}'.format(meta)

if __name__ == '__main__':
    app.run(debug=True)

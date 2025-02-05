from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', name=__name__)

if __name__ == '__main__':
  app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return 'IT IS INDEX PAGE'

if __name__ == '__main__':
  app.run(debug=True)
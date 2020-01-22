from flask import Flask, render_template
from flask_cors import CORS

#config
DEBUG = True

app = Flask(__name__,template_folder='../dist',static_folder='../static')
app.config.from_object(__name__)

CORS(app,resources={r'/*': {'origins':'*'}})

@app.route('/test', methods=['GET'])
def test():
  return jsonify('help!')

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
  app.run('0.0.0.0')

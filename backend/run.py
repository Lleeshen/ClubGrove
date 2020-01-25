from flask import Flask, current_app, jsonify, render_template
#from flask_cors import CORS
import os

#config
DEBUG = True

app = Flask(__name__,template_folder='../dist',static_folder='../static')
app.config.from_object(__name__)

jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    variable_start_string='%%',
    variable_end_string='%%'
))
app.jinja_options = jinja_options

#CORS(app,resources={r'/*': {'origins':'*'}})

@app.route('/test', methods=['GET'])
def test():
  return jsonify('help!')

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
  app.run('0.0.0.0')
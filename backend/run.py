from flask import Flask, current_app, jsonify, render_template
import os

# config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

jinja_options = app.jinja_options.copy()
jinja_options.update(dict(
    variable_start_string='%%',
    variable_end_string='%%'
))
app.jinja_options = jinja_options

@app.route('/test', methods=['GET'])
def test():
  return render_template(entry)
if __name__ == '__main__':
  app.run('0.0.0.0')

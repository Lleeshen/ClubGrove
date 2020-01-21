from flask import Flask, jsonify

# config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/test', methods=['GET'])
def test():
  return jsonify('help!')
if __name__ == '__main__':
  app.run('0.0.0.0')

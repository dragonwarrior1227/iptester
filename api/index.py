from flask import Flask, render_template,jsonify, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world'


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/ipt')
def get_tasks():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:

        return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200


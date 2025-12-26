from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/home', methods=['GET', 'POST'])
def home():
    age = request.args.get('age')
    pwd = request.args.get('pwd')
    print(age, pwd)

    xx = request.form.get('xx')
    yy = request.form.get('yy')
    print(xx, yy)

    return jsonify({
        'status': 'success',
        'result': {
            'age': age
        }
    })



@app.route('/bili', methods=['POST'])
def bili():
    pass


if __name__ == '__main__':
    app.run()

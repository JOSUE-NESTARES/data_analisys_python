from flask import Flask

app = Flask(__name__)

@app.route('/api/home') # url.com/api/home
def hello():
    return 'Hola Mundo desde Docker'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
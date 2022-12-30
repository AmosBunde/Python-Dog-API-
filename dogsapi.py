from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)



@app.route('/')
def me():
    return 'I am who I am'

if __name__ == '__main__':
    app.run(debug=True)   
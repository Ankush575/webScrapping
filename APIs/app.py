# main file where the server is created and running
from flask import Flask
from routes.studentRoute import student_routes

app = Flask(__name__)

app.register_blueprint(student_routes)


@app.route('/')
def home():
    return "Hello, Flask Server has been started!"


if __name__ == '__main__':
    app.run(debug=True)

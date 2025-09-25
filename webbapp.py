from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def root():
    template = open('greet.html').read()
    return template.replace("{result}", "World")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    name = request.values.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
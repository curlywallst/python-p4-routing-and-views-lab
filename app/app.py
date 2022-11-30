#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:word>')
def print_string(word):
    print(f'{word}')
    return f'{word}'

@app.route('/count/<int:num>')
def count(num):
    string = ''
    for x in range(num):
        string = string + str(x) + "\n"
        # print(str)

    return f'{string}'

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        return f'{num1 / num2}'
    elif operation == '%':
        return f'{num1 % num2}'

# @app.route('/<username>')
# def user(username):
#     return f'<h1>Profile for {username}</h1>'


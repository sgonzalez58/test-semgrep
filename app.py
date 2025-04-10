from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    x = eval(input("Enter a number: "))
    return "hello world !\n Your number is {}".format(x)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 

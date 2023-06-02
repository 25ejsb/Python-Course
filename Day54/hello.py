from flask import Flask
app = Flask(__name__)

# use $export FLASK_APP=[scriptname]
# use $python -m flask run
# on server 127.0.0.1:5000

# bash command $rm -rf is really powerful >:)

@app.route('/')
def hello_world():
    return "<h1 style='color:red;'>Hello, World!</h1>" \
    "<p style='font-size: 32px'>This is a paragraph</p>" \
    "<img src='https://www.ikea.com/us/en/images/products/oeverskadlig-french-door-refrigerator-stainless-steel__0956636_pe804803_s5.jpg?f=s' alt='Hmm'>"

@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/username/<path:name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are number {number}"

if __name__ == '__main__':
    app.run(debug=True)
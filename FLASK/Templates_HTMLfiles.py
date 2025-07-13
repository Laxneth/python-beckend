from re import S
from flask import Flask, render_template, redirect, url_for

# Initialize the Flask app and set the templates folder
app = Flask(__name__, template_folder='templates')

# Home route
@app.route('/')
def index():
    myname = 'aykut'                      # Variable to be passed to template
    myresult = 10 + 20                   # Simple calculation
    mylist = [10, 20, 30, 40, 50]        # List to loop in template
    return render_template("index.html", my_name=myname, my_result=myresult, mylist=mylist)

# A secondary static page
@app.route('/other')
def other():
    return render_template("other.html")

# Custom filter: reverses a string
@app.template_filter('reverse_string')
def reverse_string_filter(s):
    return s[::-1]

# Custom filter: repeats a string
@app.template_filter('repeat')
def repeat(s, time=2):
    return s * time

# Custom filter: alternates casing of characters (e.g. HeLlO WoRlD)
@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

# Filters route to demonstrate filters
@app.route('/filters')
def filters():
    some_text = "Hello world"
    return render_template("filters.html", some_text=some_text)

# Route that redirects to the filters page
@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('filters'))

# Another static page
@app.route("/derin") 
def derin():
    return render_template("derin.html")

# Run the app in debug mode, accessible from any IP
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

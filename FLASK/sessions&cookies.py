from flask import Flask, render_template, session, make_response, request, flash

# Create a Flask app instance
app = Flask(__name__, template_folder='templates')

# Secret key is required for session and flash messages
app.secret_key = 'SOME KEY'

# Home page route
@app.route('/')
def index():
    return render_template('session.html')

# Set session data
@app.route('/set_data')
def set_data():
    session['name'] = 'Aykut'
    session['other'] = 'Hello World'
    return render_template('session.html', message="Session Data Set")

# Retrieve session data
@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('session.html', message=f'Name: {name}, Other: {other}')
    else:
        return render_template('session.html', message='No session found')

# Clear all session data
@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('session.html', message='Session Cleared')

# Set a browser cookie
@app.route("/set_cookie")
def set_cookie():
    response = make_response(render_template('session.html', message='Cookie Set'))
    response.set_cookie('cookie_name', 'cookie_value')  # Set a cookie with name and value
    return response

# Get the value of a browser cookie
@app.route("/get_cookie")
def get_cookie():
    cookie_value = request.cookies.get('cookie_name')
    return render_template('session.html', message=f'Cookie Value: {cookie_value}')

# Remove a browser cookie by setting its expiry to 0
@app.route("/remove_cookie")
def remove_cookie():
    response = make_response(render_template('session.html', message='Cookie Removed'))
    response.set_cookie('cookie_name', expires=0)
    return response

# Login route (GET to show form, POST to process login)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Show the login form
        return render_template('login.html')
    elif request.method == 'POST':
        # Get username and password from the form
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'laxneth' and password == 'password':
            flash('Successful Login!')  # Show success message
            return render_template('session.html', message='')
        else:
            flash('Unsuccessful Login. Please try again!')  # Show error message
            return render_template('login.html', message='')

# Run the Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

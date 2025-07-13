from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello Word"

#URL processor
# GET: get info  #POST: create/submit info  #PUT:change info #DELETE:delete info
@app.route('/hello', methods = ['GET','POST']) # say the route of this function runs
def hello():
    if request.method == 'GET' :#differentiate methods
        return  ' You made a GET request'
    elif request.method == 'POST' :#differentiate methods
        return  ' You made a POST request'
    else : 
        return "You will never see this message"
    return "Hello World!!!"


@app.route('/greet/<name>') #/greet/name will be dynamic
def greet(name):
    return f"Hello {name}"

@app.route('/add/<number1>/<number2>') 
#we can pass number 1 as an intiger directly without typecasting : <int:number1>
def add(number1,number2):
    number1 = int(number1)
    number2 = int(number2)
    return f'{number1} + {number2} = {number1 + number2}'

@app.route('/handle_url_params')
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
        greeting = request.args['greeting']  
        name = request.args.get('name') #both ways are same
        return f'{greeting},{name}'
    else: 
        return 'some paramters are missing'

@app.route("/response") #creating custom responses
def hello2():
    response = make_response('Response is successful')
    response.status_code = 202
    response.headers['content-type'] = "text/plain"
    return response


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5555, debug=True)

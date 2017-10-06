from flask import Flask, request
from flask_restful import Resource, Api, abort
import arrow

app = Flask(__name__)
api = Api(app)


## HTTP GET request to '/date' 
class Date(Resource):
  def get(self):
    return arrow.now().format('YYYY-MM-DD')

## HTTP GET request to '/hello'
class Hello(Resource):
  def get(self):
    queryFormat = '/hello?firstname={first name}&lastname={last name}&gender={m/f}'
    genders = {'m': 'Mr', 'f': 'Ms'}

    if len(request.args) < 3:
      abort(400, statusCode=400, message= 'Insufficient number of params', action='Please supply a valid query in form of:' + queryFormat)

    if len(request.args['first_name']) > 0 and len(request.args['last_name']) > 0: 
      if request.args['gender'] in genders.keys(): 
        return "Hello {} {} {}".format(genders[request.args['gender']], request.args['first_name'].capitalize(), request.args['last_name'].capitalize())
      else:
        abort(400, statusCode=400,  message='Unknown gender option', action= 'Please supply a gender as a query string in this format: `gender={m/f}`')
    else: 
      abort(400, statusCode=400, message='Invalid query: empty string for one or both name inputs', action= 'Please supply a valid query string in the format:' + queryFormat)

## helper methods for Compute

def isInteger(value):
  return isinstance(value, int)

def performOperation(operator, a, b):
  if operator == 'add':
    return a+b
  if operator == 'subtract':
    return a-b
  if operator =='multiply':
    return a*b
  if operator =='divide':
    return a/b

## HTTP GET request to '/compute'
class Compute(Resource):

  def get(self):
    queryFormat = '/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}'
    validOperators = 'add/subtract/divide/multiply'
    operators = ['add', 'subtract', 'divide','multiply']

    if len(request.args) < 3:
      abort(400, statusCode=400, message= 'Insufficient number of params', action='Please supply a valid query in form of:' + queryFormat)

    operator = request.args['operator']

    try: 
      if isInteger(int(request.args['num1'])) and isInteger(int(request.args['num2'])):
        if operator in operators:
           return performOperation(operator, int(request.args['num1']), int(request.args['num2']))
        else:
          abort(400, statusCode=400, message='Invalid operator option', action = 'Please supply a valid operator in your query string. Your options are:' + validOperators )
    
    except: 
      abort(400, statusCode=400, message='Invalid param type - Could not convert num1/num2 to number', action='Please supply valid numbers as num1 and num2 in the format:' + queryFormat)


api.add_resource(Date, '/date')
api.add_resource(Hello, '/hello')
api.add_resource(Compute, '/compute')

if __name__ == '__main__':
    app.run()

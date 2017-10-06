#### Welcome to pAPI

This simple RESTful API supports requests to 3 endpoints ```'/date'```, ```'/compute'``` and ```'/hello'```. See API Methods for detailed explanations and examples of requests and responses.



### Running a local copy
1. Fork and clone this repo
2. Make a virtual environment: ```$ mkvirtualenv <NAME>```.
2. Install the API's dependencies  ``` $ pip install -r requirements.txt ```
3. Start the server:  ``` $ python app.py ```
 
 
### API Methods

In order to illustrate the functionality of this API, I'll be using some example data. Below are example requests - both successful and unsuccessful. 

###  1) GET ```/hello```

  Params   | Data type   | Description |Allowable Content |
| ------------- |:-------------:| -----:| -----:
| first_name     | String| Required | Any non-empty string
| last_name      | String      |   Required | Any non-empty string
| gender     | String      |   Required |  'm' or 'f'   |


**Functionality**: Given a ```gender(m or f)``` and a ```first_name``` and ```last_name```, respond with ```Mr/Ms``````first_name``` ```last_name```

#### Succesful example request


```$ curl base_url/hello?first_name=tier&last_name=nguyen&gender=m ```

#### Succesful example response

The response to the above request will be

``` "Hello Mr Tier Nguyen``` with a ``` Status code - 200 OK```

#### Unsuccesful requests

There are multiple ways that a client might send a wrong request to this endpoint. Here are three examples: 

##### Example request 1 - Insufficient number of params

If the user sends an insufficient number of query-strings e.g. if a client sends a request with a ```first_name ```and ```last_name``` but no ```gender```. This might look like:

``` $ curl base_url/hello?first_name=tier&last_name=nguyen```

The response from the API would look like:

``` Status code - 400 Bad Request```

``` {
    "statusCode": 400,
    "message": "Insufficient number of params",
    "action": "Please supply a valid query in form of:/hello?firstname={first name}&lastname={last name}&gender={m/f}"
}
```
##### Example request 2 - Empty strings

If the user sends the correct number of query-strings but sends an empty string for one or more of the params. This might look like: 

``` $ curl base_url/hello?first_name=&last_name=&gender=m```

The response from the API will look like: 

``` Status code - 400 Bad Request```

```
{
  "statusCode": 400,
  "message": "Invalid query: empty string for one or both name inputs",
  "action": "Please supply a valid query string in the format:/hello?firstname={first name}&lastname={last name}&gender={m/f}"
}
```

##### Example request 3 - Invalid param choice

The user might send the correct number of query-strings but choose an gender option that is not ```'m'``` or ```'f'```. This might look like this:

``` $ curl base_url/hello?first_name=tier&last_name=nguyen&gender=x```


The response from the API will look like: 

``` Status code - 400 Bad Request```

```
{
    "statusCode": 400,
    "message": "Unknown gender option",
    "action": "Please supply a gender as a query string in this format: `gender={m/f}`"
}
```

###  2) GET ```/compute```

**Functionality**: Take two numbers (integers) and perform a basic arithmetic operation on them - add, subtract, multiply, divide.

 Params   | Data type   | Description |Options |
| ------------- |:-------------:| -----:| -----:
| num1     | Int | Required | Any integer |
| num2      | Int     |   Required | Any integer | 
|operator   | String      |   Required |  add, subtract, multiply or divide|



#### Successful Request

Let's imagine the user wants to divide 200 by 10 to yield.

The request will look like: 

```$ curl 'base_url/compute?num1=200&num2=10&operator=divide'```

or ``` $ curl base_url/compute\?num1\=200\&num2\=10\&operator\=divide ```

#### Successful Response

The response will be: ``` 20.0 ```  with a ``` Status code - 200 OK```

#### Unsuccesful Request

There are many ways a client might make a bad request. Here are 3 examples: 

##### Example 1 - Invalid operator 

The user might want to exponentiate i.e. raise num1 to the power of num2 in the form```num1 ^ num2 ```. This functionality is not supported by this API. 


The request might look like: ```  $ curl  'base_url/compute?num1=200&num2=10&operator=exponentiate'```

Similarly, the user might send a typo or mispelled operator e.g. ```divid ``` instead of ```divide```: 

```  $ curl  'base_url/compute?num1=200&num2=10&operator=divid'```

For both kinds of requests, the API will respond with: 

``` Status code - 400 Bad Request```

```
{
    "statusCode": 400,
    "message": "Invalid operator option",
    "action": "Please supply a valid operator in your query string. Your options are:add/subtract/divide/multiply"
}
```

##### Example 2 - Insufficient number of params

If the user sends fewer params than are required, the API response will look like: 

``` Status code - 400 Bad Request```

```
{
  "statusCode": 400,
  "message": "Insufficient number of params",
  "action": "Please supply a valid query in form of:/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}"
}

```

##### Example 3 - Invalid params 

The user might send a wrong type ```num1=str``` or ```num2=true``` and these values can not be converted to numbers for the operations to occur.

A bad request of this type might look like: 

```
$ curl base_url/compute?num1=x&num2=10&operator=divide
```
The API's response would look like:

``` Status code - 400 Bad Request```

```
{
  "statusCode": 400,
  "message": "Invalid param type - Could not convert num1/num2 to number",
  "action": "Please supply valid number as num1 and num2 in the format:/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}"
}
```


### 3) GET '```/ date```

**Functionality**: Retrieve today's date in YYYY-MM-DD format


#### Successful request
This will look like: ``` $ curl base_url/date ```
 
If this request was sent today (5th of October), the API response will look like: 

``` "2017-10-05" ``` with a ``` Status code - 200 OK```

 
### Next steps

Here are some ideas for building upon the functionality of this simple RESTful API: 

- Compute - extending the functionality of the ```/compute``` endpoint to support more complicated operations - square roots, powers, logarithms, rounding etc. 
- Compute - extend functionality to support operations on floats and fractions
- More input validation - more checks to ensure that the user sends the right kind of data
- More custom error handling - perhaps sending different ```4xx status codes ```for client-side errors 
- Date - extending the functionality of the ```/date``` endpoint to support other date formats e.g. "dd/mm/yy" or "mm/dd/yyyy"

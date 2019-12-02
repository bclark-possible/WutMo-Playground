Let's install [Chalice](https://chalice.readthedocs.io/en/latest/)

"AWS Chalice allows you to quickly create and deploy applications that use Amazon API Gateway and AWS Lambda."


### Install Chalice
1. Add 'chalice' to your requirements.txt
2. From inside your virtual environment run ```pip install -r requirements.txt```

### Setup environment for Chalice

1. Create a directory called ```chalicelib```
  1. This is where you will store your library code
2. Create a directory called ```vendor```
  1. This is where you will store 3rd party code
3. Move the ```modules``` directory to ```chalicelib```
4. Move the ```storage``` directory to ```chalicelib```
5. Update any references to include chalicelib now
  1. i.e. ```from modules.Weather import Weather``` -> ```from chalicelib.modules.Weather import Weather```


To make things a little easier, comment out all your methods in _app.py_ except ```index()```, ```hello()```, and ```weather(city)```

You can also comment out all storage and module imports except for _Weather_

Once all imports have been corrected we are ready to run locally

### Running locally

1. Use ```chalice local``` to run
2. If everything goes smoothly you should have a server running on http://127.0.0.8:8000
3. Try the following paths http://127.0.0.8:8000/hello & http://127.0.0.8:8000/weather/Atlanta
4. You should see the requests come in ```"GET /hello HTTP/1.1" 200 -``` & ```"GET /weather/Atlanta HTTP/1.1" 200 -```
5. You can stop the server

### Deploying to AWS

Chalice will create a Lambda and API Gateway for you in AWS.

1. Simply type ```chalice deploy```
2. You will get your Lambda ARN & and a REST API URL for your API Gateway
3. Test your paths with your new URL

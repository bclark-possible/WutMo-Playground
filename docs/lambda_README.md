Using AWS Lambda and API Gateway

1. Create new lambda function
2. Choose **Python 3.7** _Runtime_
3. Click _Create Function_
4. Create a ```lambda_function.py``` in your project root directory.

## API Gateway

1. Click _Create API_
2. Choose _REST_
3. Choose _New API_
4. Name It
5. Click _Create API_

### Creating Your First Resource

1. Click the _Actions_ button
2. Choose _Create Method_
3. Select _GET_
4. Retrieve your Lambda ARN (top right in your Lambda)
5. Click _Test_ in the Method Execution section.
6. Click the _Test_ button  
7. You should receive a **Status: 200**

## Connecting API Gateway to Lambda

1. Create a stage for your API Gateway
  1. Click the _Actions_ button
  2. Choose _Deploy API_
  3. From _Deployment Stage_ choose _[New Stage]_
  4. Name it 'Dev'
  5. Stage description can be 'development'
  6. Click _Deploy_
  7. You should now have a URL


From your Lambda configuration click _Add trigger_
1. Choose _API Gateway_
2. Pick your API
3. Choose your _Deployment Stage_ should be 'Dev'
4. For Security choose 'Open', this will make your API public.

**You should now be able to navigate to the URL and see 'Hello from Lambda!'**

### Adding a new API Resource (Endpoint)

1. Click _Actions_ and choose _Create Resource_
2. For _Resource Name_ put 'Weather'
3. For _Resource Path_ put 'weather'
4. Hit _Create Resource_
5. This will set you up to add new parameter based endpoints
6. Now add a Method
  1. Click '/weather' and then Click _Actions_
  2. Choose _Create Method_
  3. Choose _GET_
  4. Pick _AWS Lambda_ and paste your Lambda's ARN
  5. Expand _URL Query String Parameters_
  6. Click _Add query string_
  7. Enter in 'city' for the name and then click the check mark on the right
7. We need to setup how API Gateway will send this to our lambda using a mapping template
  1. From the Method Execution screen, click _Integration Request_
  2. Scroll to the bottom and expand _Mapping Templates_
  3. Check _When there are no templates defined (recommended)_
  4. Click _Add mapping template_
  5. Use **application/json** as the content type
  6. In the _General Template_ drop down select _Method Request passthrough_
  7. Click _Save_
8. _Deploy API_

Let's add a little bit of code to the Lambda via the **Lambda Management Console**

In you ```lambda_function.py``` lets add some print statements

```python
def lambda_handler(event, context):
    print('event:',event)
    print('context:',context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

This will print in to the logs ([Cloudwatch](https://aws.amazon.com/cloudwatch/)), and we will get to this in a minute.

**You should now be able to navigate to the URL/weather?city=Atlanta and STILL see 'Hello from Lambda!'**

But where did 'Atlanta' go , and what about our use of '/weather'?

1. back to **Lambda Management Console** and click _Monitoring_ on the left side.
2. Now Click _View logs in Cloudwatch_ on the right side
3. Logs are bunched into streams, you may only have 1, but click the most recent.
4. You should see ```event: {'city': 'Atlanta'}```
5. You now have access to this in your lambda!

Let's try it out, using Lambda Tests

1. Modify your lambda to handle the new parameter

```Python
def lambda_handler(event, context):
    print('event:',event)
    print('context:',context)

    message = json.dumps(event)

    if 'city' in event:
        message = handle_city_weather(event['city'],context)

    response = {
        'statusCode': 200,
        'body': json.dumps(message)
    }

    return response

def handle_city_weather(city, context):
    message = ""

    if len(city) == 0:
        return "No city specified"

    try:
        message = 'Looking for the weather in {0}'.format(city)
    except :
        pass

    return message
```
2. Click _Configure test events_ at the top right
3. Name it 'CityWeatherTest'
4. Past in the following json

```json
{"city": "Atlanta"}
```
5. Click _Save_
6. Now choose your new test event and click _Test_
7. You should now get an Execution results box at the top with the following results

```json
{
  "statusCode": 200,
  "body": "\"Looking for the weather in Atlanta\""
}
```

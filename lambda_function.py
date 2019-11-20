import json

def lambda_handler(event, context):
    # TODO implement
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

if __name__ == "__main__":
    print("let's go!")
    event = {'city':'Atlanta'}
    context = {}
    response = lambda_handler(event, context)
    print("response:",response)
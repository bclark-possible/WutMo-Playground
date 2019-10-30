
'''
Demo Flask App using some API's from
https://github.com/public-apis/public-apis#development
'''
from flask import Flask, jsonify, escape, request
import requests
import redis

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/weather/<city>',methods=['GET'])
def weather(city):
    city_name = escape(city)
    
    try:
        city_info = get_city_info(city_name)
        woeid = city_info[0]['woeid']
        weather = get_city_weather(woeid)
    
        return weather
    except :
        print('no woeid')
    return jsonify(city=city_name,
                   error='could not find location')

@app.route('/ram/character',methods=['POST'])
def get_ram_character():
    try:
        character_id = request.get_json()['character_id']
        character = get_a_character(character_id)
        __save_character(character)
        return character
    except: 
        print('error getting character id')
    return jsonify(error='error getting character id')

'''
https://www.metaweather.com/api/
'''
def get_city_info(city_name):
    url = 'https://www.metaweather.com/api/location/search/?query={}'.format(city_name)
    return __make_request(url)

def get_city_weather(woeid):
    url = 'https://www.metaweather.com/api/location/{}/'.format(woeid)
    return __make_request(url)

'''
https://rickandmortyapi.com
'''
def get_a_character(character_id):
    if character_id < 1 or character_id > 493:
        character_id = 1
    url = 'https://rickandmortyapi.com/api/character/{}'.format(character_id)
    return __make_request(url)

'''
basic generic url requester
'''
def __make_request(url):
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    print('no response')
    return {}

'''
Data Storage via redis
https://redislabs.com/get-started-with-redis/
'''
def __save_character(character):
    try:
        c_id = character["id"]
        c_name = character["name"]
        r = redis.Redis(
            host='127.0.0.1',
            port='6379')
        r.set(c_name,c_id)
    except:
        print("Invalid character")

def __get_character_by_name(character_name):
    try:
        r = redis.Redis(
            host='127.0.0.1',
            port='6379')
        return r.get(character_name)
    except:
        print("Error getting character by name")
    return {}

if __name__ == '__main__':
    print("Starting Flask Demo")
    app.run()
'''
Demo Flask App using some API's from
https://github.com/public-apis/public-apis#development
'''
# from flask import Flask, jsonify, escape, request
from chalice import Chalice, Response
import html
from chalicelib.modules.Weather import Weather
from chalicelib.modules.RickAndMorty import RickAndMorty
from chalicelib.storage.SimpleRedisStorage import SimpleRedisStorage

REDIS_URI = '127.0.0.1'
REDIS_PORT = '6379'

# app = Flask(__name__)
app = Chalice(app_name="wutmo-demo")
app.debug = True

def create_response(body, status_code = 200):
    return Response(status_code=status_code,
                    headers={'Content-Type': 'application/json'},
                    body=body)

@app.route('/')
def index():
    body = 'Hack the Planet!<br /><img src="https://media.giphy.com/media/lzfWemZZMfb2M/giphy.gif" />'
    return Response(body=body,
                    status_code=200,
                    headers={'Content-Type': 'text/html'})

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/weather/{city}',methods=['GET'])
def weather(city):
    city_name = html.unescape(city)
    print(city_name)

    w = Weather()

    city_info = w.get_city_info(city_name)
    print(city_info)
    woeid = city_info[0]['woeid']
    weather = w.get_city_weather(woeid)

    return weather
    
    try:
        w = Weather()

        city_info = w.get_city_info(city_name)
        print(city_info)
        woeid = city_info[0]['woeid']
        weather = w.get_city_weather(woeid)
    
        return weather
    except :
        print('no woeid')
    return {'city':city_name,'error':'error getting character id'}

# @app.route('/ram/character',methods=['POST'])
# def get_ram_character():
#     character = None
#     try:
#         ram = RickAndMorty()

#         character_id = request.get_json()['character_id']
#         character_id = int(character_id)
#         character = ram.get_a_character(character_id)
        
#     except: 
#         print('error getting character id')

#     if __save_character(character) is None:
#             print('Error saving character')
            
#     if character is not None:
#         return character

#     return {'error':'error getting character id'}



@app.route('/ram/get_character/{character_id}',methods=['GET'])
def get_ram_get_character(character_id):
    
    character = None
    try:
        ram = RickAndMorty()
        print(character_id,type(character_id))
        character_id = int(character_id)
        print(character_id,type(character_id))
        
    except: 
        print('error getting character id')

    character = ram.get_a_character(character_id)

    if __save_character(character) is None:
            print('Error saving character')
            
    if character is not None:
        return create_response(character)

    error_response = {"error":'error getting character id',"character":character_id}
    return create_response(error_response, 400)

def __save_character(character):
    print("Saving Character")
    
    try:
        c_id = character["id"]
        c_name = character["name"]
        storage = SimpleRedisStorage(REDIS_URI,REDIS_PORT)
        return storage.set(c_name,c_id)
    except:
        print("Invalid character")
    return None

def __get_character_by_name(character_name):
    try:
        storage = SimpleRedisStorage(REDIS_URI,REDIS_PORT)
        return storage.get(character_name)
    except:
        print("Error getting character by name")
    return {}
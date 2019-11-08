
'''
Demo Flask App using some API's from
https://github.com/public-apis/public-apis#development
'''
from flask import Flask, jsonify, escape, request
# import requests
# import redis
from modules.Weather import Weather
# from modules.RickAndMorty import RickAndMorty
# from storage.SimpleRedisStorage import SimpleRedisStorage

application = Flask(__name__)

@application.route('/hello')
def hello():
    return 'Hello World!'

@application.route('/weather/<city>',methods=['GET'])
def weather(city):
    city_name = escape(city)
    
    try:
        w = Weather()

        city_info = w.get_city_info(city_name)
        woeid = city_info[0]['woeid']
        weather = w.get_city_weather(woeid)
    
        return weather
    except :
        print('no woeid')
    return jsonify(city=city_name,
                   error='could not find location')

# @app.route('/ram/character',methods=['POST'])
# def get_ram_character():
#     character = None
#     try:
#         ram = RickAndMorty()

#         character_id = request.get_json()['character_id']
#         character = ram.get_a_character(character_id)
        
#     except: 
#         print('error getting character id')

#     if __save_character(character) is None:
#             print('Error saving character')
            
#     if character is not None:
#         return character

#     return jsonify(error='error getting character id')

# def __save_character(character):
#     c_id = character["id"]
#     c_name = character["name"]
#     storage = SimpleRedisStorage('127.0.0.1','6379')
#     return storage.set(c_name,c_id)

#     try:
#         c_id = character["id"]
#         c_name = character["name"]
#         storage = SimpleRedisStorage('127.0.0.1','6379')
#         return storage.set(c_name,c_id)
#     except:
#         print("Invalid character")
#     return None

# def __get_character_by_name(character_name):
#     try:
#         storage = SimpleRedisStorage('127.0.0.1','6379')
#         return storage.get(character_name)
#     except:
#         print("Error getting character by name")
#     return {}
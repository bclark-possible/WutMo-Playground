# Flask-Demo

## Goal

A simple Flask/Redis demo, to showcase how to build a simple service/API from your local machine. We will take this example and build new concepts on to it. 

- [Python 3](https://www.saintlad.com/install-python-3-on-mac/) Use the Homebrew way
- [Homebrew](https://brew.sh)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)
- [Redis](https://redislabs.com/get-started-with-redis/)
- [Virtual Studio Code](https://code.visualstudio.com)
- [Docker](https://www.docker.com)
- [Postman](https://www.getpostman.com)

/******************************************************
### Please contribute and add new features, and put them up for PR!  
### This should be a fun project to learn with. 
******************************************************/

## How to Run

1. Create virtual environment
   1. From terminal in root directory type `python3 -m venv ./venv`
2. Activate virtual environment `source venv/bin/activate`
3. Install dependencies `pip install -r requirements.txt`
4. Setup redis
   1. From a terminal run `brew install Redis`
   2. Start Redis `brew services start Redis`
   3. Verify with `redis-cli`
      1. Type `ping`, should receive `PONG`
   4. Hit `Ctrl+C` to exit
5. Run app `python app.py`

This will kick off a service running on http://127.0.0.1:5000

## How to Contribute

If you would like to add functionality here are some examples
- Add new endpoints
- Modify existing endpoints
- Add new modules, that connect to different API's
- Add new storage classes to keep the data saved or cached to reduce network calls


## Endpoints

- ### /hello
        returns 'Hello World!`

- ### [GET] /weather/\<city\>
        attempts to fetch weather data for the passed in city
        returns weather data JSON

- ### [POST] /ram/character/\<character_id\>
        takes an integer from 1-493 that represents a character idea
        saves 
        returns JSON for the given Rick & Morty character

## Modules

- Weather - connects to https://www.metaweather.com/api/
- RickAndMorty - connects to https://rickandmortyapi.com
  

## Storage

- SimpleDataStorage - Abstract class with ```set(key, value)``` & ```get(key)```
- SimpleRedisStorage - Takes a host and port, and then uses ```set(key, value)``` & ```get(key)```

## Docker

This project does come with a Dockerfile to build a docker image, but currently having troubles accessing the server once it is running. 

### How to build

1. First install Docker
2. Make sure docker is running
3. From a terminal run `docker build -t flask_demo .`, this step will take awhile
4. verify by typing `docker images`
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
flask_demo          latest              64efffd15d33        3 hours ago         517MB
```
5. Now run the image `docker run -p 127.0.0.1:5000:5000 flask_demo`
6. Verify in another terminal by typing `docker container ls`
```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                      NAMES
8400f5fe1b9e        flask_demo          "python3 app.py"    11 seconds ago      Up 10 seconds       127.0.0.1:8888->5000/tcp   clever_tharp
```
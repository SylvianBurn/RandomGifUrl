import json
from flask import Flask, jsonify
import requests
from faker import Faker

fake = Faker()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    response = "Hello World !"
    return response

@app.route("/random", methods=["GET"])
def randomGIF():
    newFirstName = fake.first_name()
    newLastName = fake.last_name()
    req = requests.get('https://api.giphy.com/v1/gifs/random?api_key=xKoI2wYWT9ulyMCh7TbE6jwNkeASoTaR&tag=&rating=g').json()
    urlRandom = req.get('data').get('url')
    return jsonify({'prenom': newFirstName,
                    'nom': newLastName,
                    'urlGif': urlRandom})

if __name__ == "__main__":
    app.run()
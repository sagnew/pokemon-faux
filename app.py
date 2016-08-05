import random

import requests
from flask import Flask, request, send_from_directory
from twilio import twiml

from overlay import overlay

UPLOAD_FOLDER = '/Path/to/your/code/directory'
legendary_pokemon = ['articuno', 'zapdos', 'moltres', 'mewtwo', 'mew']

app = Flask(__name__)


@app.route('/sms', methods=['POST', 'GET'])
def sms():
    # Generate TwiML to respond to the message.
    response = twiml.Response()
    response.message("Please wait while we try to catch your Pokemon")

    if request.form['NumMedia'] != '0':

        # Default to Mew if no Pokemon is selected.
        if request.form['Body']:
            # Take the first word they sent, and convert it to lowercase.
            pokemon = request.form['Body'].split()[0].lower()
            if not pokemon in legendary_pokemon:
                pokemon = random.choice(legendary_pokemon)
        else:
            pokemon = random.choice(legendary_pokemon)

        # Save the image to a new file.
        filename = request.form['MessageSid'] + '.png'
        with open('{}/{}'.format(UPLOAD_FOLDER, filename), 'wb') as f:
           image_url = request.form['MediaUrl0']
           f.write(requests.get(image_url).content)

        # Manipulate the image.
        overlay('{}/{}'.format(UPLOAD_FOLDER, filename), pokemon)

        # Respond to the text message.
        with response.message() as message:
            message.body = "{0}".format("Congrats on the sweet catch.")
            message.media('http://{your_ngrok_url}/uploads/{}'.format(filename))
    else:
        response.message("Send me an image that you want to catch a Pokemon on!")

    return str(response)


@app.route('/uploads/<filename>', methods=['GET', 'POST'])
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER,
                               filename)


@app.route('/voice', methods=['GET', 'POST'])
def uploaded_file(filename):
    resp = twiml.Response()
    resp.play('https://www.dropbox.com/s/gug2oovnsymo4zp/pokemon.mp3?dl=1')
    return str(resp)

if __name__ == "__main__":
    app.run()

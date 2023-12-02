import os
from flask import Flask , render_template , redirect , url_for , send_file
from twilio.rest import Client

app = Flask(__name__)

# Route and define the index function to render the home.html.
@app.route('/')
def index():
	return render_template('home.html')

# Call the app.run()
if __name__ == "__main__":
	app.run()



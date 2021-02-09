import random
from flask import Flask, render_template

app = Flask(__name__)

emotions = ['anger','contempt','disgust','fear','happiness','sadness','surprise']

@app.route('/')
def home():
  page_data = {
    'emotion' : random.choice(emotions)
  }
  return render_template('home.html', page_data = page_data)
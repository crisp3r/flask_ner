from flask import Flask, request, json
from flask_cors import CORS
import flask
from ner_client import NamedEntityClient
import spacy

app = Flask(__name__)
CORS(app) # https://flask-cors.readthedocs.io/en/latest/#:~:text=A%20Flask%20extension%20for%20handling,allowed%20headers%2C%20methods%2C%20etc.

model = {
    'en': spacy.load('en_core_web_md'),
    'fr': None,
    'cn': None,
    'ru': None
}
def load_model(lang):
    if model[lang] is None:
        return None, f"{lang} Model not yet implented"
    try:
        ner = NamedEntityClient(model[lang])
        return ner, "Model loaded successfully"
    except:
        return None, "Error loading model"
@app.route('/')
def index():
    return "Welcom bro"

@app.route('/ner/<lang>', methods=['GET', 'POST'])
def get_ents(lang='en'):
    ner, msg = load_model(lang)
    if ner is None:
        return msg
    if request.method == 'POST':
        # client request: 
        # 'Content-Type': 'application/json'
        # {'sentence': "i luv u!"}}
        data = request.get_json()
        print(ner.get_ents(data["sentence"]))
        return json.dumps(ner.get_ents(data["sentence"]))
    return msg
from flask import Flask
from src.api.v1.urls import chat_api

app = Flask(__name__)
app.register_blueprint(chat_api)

if __name__ == "__main__":
    app.run(debug=True, port=3000)

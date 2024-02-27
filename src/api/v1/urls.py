from flask import Blueprint
from .view import LlamaResponseView

chat_api = Blueprint("chat_api", __name__)

llama_view = LlamaResponseView.as_view("chat")
chat_api.add_url_rule("/chat", view_func=llama_view, methods=["POST"])

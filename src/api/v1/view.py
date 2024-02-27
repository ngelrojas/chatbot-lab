from flask.views import MethodView
from flask import request, jsonify
from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate


class LlamaResponseView(MethodView):
    def __init__(self):
        self.llm = CTransformers(
            model="models/llama-2-7b-chat.ggmlv3.q2_K.bin",
            model_type="llama",
            config={"max_new_tokens": 256, "temperature": 0.01},
        )

    def get_llama_response(self, input_text, no_words, blog_style):
        template = """
            Write a blog for {blog_style} job profile for a topic {input_text}
            within {no_words} words.
                """

        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", "no_words"], template=template
        )

        response = self.llm(
            prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
        )

        return response

    def post(self):
        data = request.get_json()
        input_text = data.get("input_text")
        no_words = data.get("no_words")
        blog_style = data.get("blog_style")
        response = self.get_llama_response(input_text, no_words, blog_style)
        return jsonify({"data": response})

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from request import get_recipe

app = Flask(__name__)

line_bot_api  = LineBotApi('YfN0O0lBlm3op1TSJh9NdPoZlwkRDxEfbgaSfDE7QBN+meYvrvQtGpLa1lQJy3m8dj38cYQZmAQwrJQzOd7oJ9Bgq8f00LQwpkXqgbXFmBBF5lemc5jq4krOo6uTfNVRF6uuwc+NNyA9OrFVsQ+2MgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('45262b6352a751b2bcfdb258cad68bd2')

@app.route('/')
def test():
    return 'hello'


    
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #関数呼び出し
    recipe = get_recipe(event.message.text)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = recipe))

if __name__ == "__main__":
    app.run()
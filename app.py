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

line_bot_api  = LineBotApi('6Rh79OVL8PEWzFPUfFS4Elfc1Tz0J+Jiz5pOE2OGsagUXbzdQU+2e/1vDh+DMPZLdj38cYQZmAQwrJQzOd7oJ9Bgq8f00LQwpkXqgbXFmBAC4OvV4U5qemRYO8ikePJBA5mEw/rSTJUKf0mWQpOEFgdB04t89/1O/w1cDnyilFU=')
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

    datas = ({
        "data":[]
    })

    print(event.message.text)

    datas["data"].append(str(event.message.text))

    recipe = get_recipe(datas)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=recipe))

if __name__ == "__main__":
    app.run()
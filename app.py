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

app = Flask(__name__)

line_bot_api = LineBotApi('2JTSJy3IKWqOqycGv+zmjliCGYyPVWq4mV9TVOtiKFjs5JqfZsLNpKRMrL2PFWCWtk4YsVRAt2tkpoWPuohiIlS0NvVcZ3DmO1z5J+xrl/fJzzb2y1vBD2J8QO2QUcaXFkpGJ32iBj/4noMLgfmmhwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d6b1a9c7594e52ea3a20e59301ef872a')

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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
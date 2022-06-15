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



line_bot_api  = LineBotApi('lc06w+nVr75SvVKOhl8M2xADbTuAz3leAufGlFTFyzOR6gs5QNwTKmZtKgY0+JhaylLsBi9k5SDN1UWXrfWeQ5A7cke7B/Cbf+SOD5hEQDu8k6HCDN6jdwd3XgTELhe6Nbsm7tru5pNWKb1mwESsVwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7d4332f03ff00004579df188b77bcfb2')

@app.route('/')
def test():
    a = print(get_recipe('鶏肉'))
    return str(a)
    


    
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
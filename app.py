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

line_bot_api = LineBotApi('mhrA92VV4GxPykpijyvgdXmwYeWdyBs+HjrMVUyjUKGIcmWtCOP7uRGVvofu073joEIUKvWLM8UMdxC2lcWyDAypMrNNlI1c9Z3cJX1rMAhxIJqBqMdM/tR595hGV8S7nQPdIzaZ8JfC5ZUGQkzOtAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0cc20cae87ede81cf9d5415198213c34')


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
    msg = event.message.text
    s = "來去看黑人吃水果！"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()

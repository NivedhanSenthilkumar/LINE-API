                                'LINE BOT'

from flask import Flask,request,abort
from linebot import (
    LineBotApi, WebhookHandler)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


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

##API
line_bot_api = linebot.LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
line_bot_api.reply_message(reply_token, TextSendMessage(text='Hello World!'))
line_bot_api.push_message(to, TextSendMessage(text='Hello World!'))
line_bot_api.multicast(['to1', 'to2'], TextSendMessage(text='Hello World!'))
line_bot_api.broadcast(TextSendMessage(text='Hello World!'))


line_bot_api.narrowcast(
    messages=TextSendMessage(text='Hello World!'),
    recipient=AudienceRecipient(group_id=5614991017776),
    filter=Filter(demographic=AgeFilter(gte="age_35", lt="age_40")),
    limit=Limit(max=10)
)

##Narrow cast INSIGHTS
narrowcast_progress = line_bot_api.get_progress_status_narrowcast(request_id)
assert narrowcast_progress.phase == 'succeeded'
print(narrowcast.success_count)
print(narrowcast.failure_count)
print(narrowcast.target_count)

##PROFILE
profile = line_bot_api.get_profile(user_id)
print(profile.display_name)
print(profile.user_id)
print(profile.picture_url)
print(profile.status_message

##GRP SUMMARY
summary = line_bot_api.get_group_summary(group_id)
print(summary.group_id)
print(summary.group_name)
print(summary.picture_url)









## MESSAGE DELIVERY COUNT
insight = line_bot_api.get_insight_message_delivery('20191231')
print(insight.api_broadcast)

#dEMOGRAPHICS
insight = line_bot_api.get_insight_demographic()
print(insight.genders)
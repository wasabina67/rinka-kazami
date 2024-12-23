import os
import random
import sys

from dotenv import load_dotenv
from linebot.v3 import messaging  # type: ignore

load_dotenv(override=True)


def main(timing, broadcast):
    user_id = os.getenv("LINE_USER_ID")
    access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    messages_by_timing = {
        "morning": [
            "おはよう！今日はどんな日にしようか？応援してるよ！",
            "おはようございます！元気いっぱいでスタートしようね！",
            "お目覚めの時間だよ～！素敵な1日を過ごしてね！",
        ],
        "sleep": [
            "おやすみなさい。今日もお疲れさま！ゆっくり休んでね。",
            "もう寝る時間だよ～。明日もいい日になりますように。おやすみ！",
            "疲れた体をしっかり休めてね。いい夢が見られますように、おやすみ！",
        ],
    }

    configuration = messaging.Configuration(access_token=access_token)
    if broadcast:
        message_dict = {
            "messages": [
                {"type": "text", "text": random.choice(messages_by_timing[timing])},
            ],
        }
    else:
        message_dict = {
            "to": user_id,
            "messages": [
                {"type": "text", "text": random.choice(messages_by_timing[timing])},
            ],
        }

    with messaging.ApiClient(configuration=configuration) as client:
        messaging_api = messaging.MessagingApi(client)
        if broadcast:
            broadcast_request = messaging.BroadcastRequest.from_dict(obj=message_dict)
            try:
                resp = messaging_api.broadcast(broadcast_request)  # noqa
                # print(resp)
            except Exception as e:
                print(e)
        else:
            push_message_request = messaging.PushMessageRequest.from_dict(obj=message_dict)
            try:
                resp = messaging_api.push_message(push_message_request)  # noqa
                # print(resp)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        timing = sys.argv[1]
        main(timing, broadcast=False)

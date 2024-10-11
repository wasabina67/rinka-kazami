import os
import random
import sys

from dotenv import load_dotenv
from linebot.v3 import messaging  # type: ignore

load_dotenv(override=True)


def main(timing):
    user_id = os.getenv("LINE_USER_ID")
    access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    messages_by_timing = {
        "morning": [
            "morning1",
            "morning2",
            "morning3",
        ],
        "sleep": [
            "sleep1",
            "sleep2",
            "sleep3",
        ],
    }

    configuration = messaging.Configuration(access_token=access_token)
    message_dict = {
        "to": user_id,
        "messages": [
            {"type": "text", "text": random.choice(messages_by_timing[timing])},
        ],
    }

    with messaging.ApiClient(configuration=configuration) as client:
        messaging_api = messaging.MessagingApi(client)
        push_message_request = messaging.PushMessageRequest.from_dict(obj=message_dict)

        try:
            resp = messaging_api.push_message(push_message_request)  # noqa
            # print(resp)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        timing = sys.argv[1]
        main(timing)

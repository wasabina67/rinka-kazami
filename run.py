import os

from dotenv import load_dotenv
from linebot.v3 import messaging

load_dotenv(override=True)


def main():
    user_id = os.getenv("LINE_USER_ID")
    access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

    config = messaging.Configuration(access_token=access_token)
    message_dict = {
        "to": user_id,
        "messages": [
            {"type": "text", "text": "text"},
        ],
    }


if __name__ == "__main__":
    main()

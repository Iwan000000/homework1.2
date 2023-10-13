from googleapiclient.discovery import build
import os

class Channel:
    def __init__(self, channel_id):
        """Данные о id канала"""

        self.channel_id = channel_id
        self.api_key = api_key = os.environ.get("YOUTUBE_API_KEY")
        self.youtube = build("youtube", "v3", developerKey=api_key)

    def print_info (self):
        """Вывод данных о канале"""

        response = self.youtube.channels().list(
            part="snippet",
            id=self.channel_id
        ).execute()
        channel_info = response["items"][0]["snippet"]
        print("Название канала:", channel_info["title"])
        print("Описание канала:", channel_info["description"])
        print("Страна:", channel_info["country"])


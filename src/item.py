from googleapiclient.discovery import build
import os
import json


class Channel:
    """
    Класс для ютуб-канала
    """
    def __init__(self, channel_id):
        """
        Данные о id канала
        :param channel_id: ID канала
        """

        self.channel_id = channel_id
        self.api_key = api_key = os.environ.get("YOUTUBE_API_KEY")
        self.youtube = self.get_service()

        response = self.youtube.channels().list(
            part="snippet,statistics",
            id=self.channel_id
        ).execute()

        channel_data = response["items"][0]
        snippet = channel_data["snippet"]
        statistics = channel_data["statistics"]

        self.channel_name = snippet["title"]
        self.description = snippet["description"]
        self.channel_link = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(statistics["subscriberCount"])
        self.video_count = int(statistics["videoCount"])
        self.view_count = int(statistics["viewCount"])

    @classmethod
    def get_service(cls):
        """
        Выводим переменную c ключом для работы с API ютуба
        :return: Выводит ключ API
        """
        api_key = os.environ.get("YOUTUBE_API_KEY")
        return build("youtube", "v3", developerKey=api_key)

    def to_json(self, filename):
        """
        Сохраняет данные канала в файл в формате JSON
        :param filename: Название файла для записи данных
        :return:
        """
        data = {
            "channel_id": self.channel_id,
            "channel_name": self.channel_name,
            "description": self.description,
            "channel_link": self.channel_link,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }
        with open(filename, "w") as file:
            json.dump(data, file)

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей
        :return: Выводит название канала и ссылку на канал
        """
        return f"{self.channel_name} ({self.channel_link})"

    def __add__(self, other):
        """
        Магический метод, который позволяет прибавлять к экземпляру класса объект произвольного типа данных
        :param other: Проинимает колличество подписчиков
        :return: Выводит сумму подписчиков двух каналов
        """
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """
        Магический метод, который позволяет вычитать от экземпляра класса
        :param other: Проинимает колличество подписчиков
        :return: Выводит результат вычитания колличества подписчиков
        """
        return self.subscriber_count - other.subscriber_count

    def __eq__(self, other):
        """
        Магический метод сравнения
        :param other: Проинимает колличество подписчиков
        :return: Выводит False если не равны и True если равны
        """
        return self.subscriber_count == other.subscriber_count

    def __lt__(self, other):
        """
        Магический метод сравнения
        :param other: Проинимает колличество подписчиков
        :return: Выводит False или True если один канал больше или меньше другого
        """
        return self.subscriber_count < other.subscriber_count

    def __ge__(self, other):
        """
        Магический метод сравнения
        :param other: Проинимает колличество подписчиков
        :return: Выводит False или True если один канал больше или меньше другого или равен
        """
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        """
        Магический метод сравнения
        :param other: Проинимает колличество подписчиков
        :return: Выводит False или True если один канал больше или меньше другого или равен
        """
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        """
        Магический метод сравнения
        :param other: Проинимает колличество подписчиков
        :return: Выводит False или True если один канал больше или меньше другого
        """
        return self.subscriber_count > other.subscriber_count


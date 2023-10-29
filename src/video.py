from googleapiclient.discovery import build
import os


class Video:
    """
    Класс для вывада данных о видио
    """

    def __init__(self, video_id):
        """
        Создание экземпляра класса
        :param video_id: id видео из ютуб
        """
        self.video_id = video_id
        youtube = Video.get_service()
        dict_to_print = youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        self.title = dict_to_print['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{dict_to_print["items"][0]["snippet"]["tags"][0]}'
        self.view_count = dict_to_print['items'][0]['statistics']['viewCount']
        self.likes_count = dict_to_print['items'][0]['statistics']['likeCount']
        self.duration = self.get_duration()
    @classmethod
    def get_service(cls):
        """
        Выводим переменную c ключом для работы с API ютуба
        :return: Выводит ключ API
        """
        api_key = os.environ.get("YOUTUBE_API_KEY")
        return build("youtube", "v3", developerKey=api_key)


    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей
        :return: Выводит информацию об объекте класса
        """
        return self.title

    def get_duration(self):
        """
        Получает продолжительность видео
        :return:Выводит продолжительность видео
        """
        youtube = Video.get_service()
        dict_to_print = youtube.videos().list(id=self.video_id, part='snippet,contentDetails').execute()
        duration = dict_to_print['items'][0]['contentDetails']['duration']
        return duration

    @property
    def url_video(self):
        """
        Возвращает URL-адрес видео
        :return:URL-адрес видео
        """
        return self.__url

class PLVideo(Video):
    """
    Класс, представляющий видео из плейлиста
    """

    def __init__(self, video_id, playlist_id):
        """
        Создание экземпляра класса
        :param video_id: id видео из ютуб
        :param playlist_id: id плейлиста, к которому принадлежит виде
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id

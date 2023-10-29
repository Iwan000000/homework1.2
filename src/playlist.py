from googleapiclient.discovery import build
import os
import isodate
from datetime import timedelta
from src.video import Video

class PlayList:
    """
    Класс для представления плейлиста на ютуб
    """
    api_key: str = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, id_playlist):
        """
        Инициализирует объект класса PlayList
        :param id_playlist: Идентификатор плейлиста
        """
        self.__id_playlist = id_playlist
        self.__info_playlist = self.get_service().playlists().list(id=self.__id_playlist, part='snippet', maxResults=50).execute()
        self.__info_videos = self.get_service().playlistItems().list(playlistId=self.__id_playlist, part='contentDetails, snippet', maxResults=50).execute()
        self.__title = self.__info_playlist['items'][0]['snippet']['title']
        self.__url = 'https://www.youtube.com/playlist?list=' + self.__id_playlist
        self.__video_ids = self.video_ids()
        self.__videos = self.videos()

    def __str__(self):
        """
        Возвращает строковое представление плейлиста
        :return:Строковое представление плейлиста
        """
        return f'{self.__title}\n{self.__url}'

    @property
    def total_duration(self):
        """
        Возвращает общую продолжительность плейлиста в виде объекта timedelta
        :return:Общая продолжительность плейлиста
        """
        result = timedelta(seconds=0)
        for video in self.__videos:
            result += isodate.parse_duration(video.duration)
        return result

    @property
    def info_playlist(self):
        """
        Возвращает информацию о плейлисте
        :return:Информация о плейлисте
        """
        return self.__info_playlist

    @property
    def url(self):
        """
        Возвращает URL плейлиста
        :return:URL плейлиста
        """
        return self.__url

    @property
    def title(self):
        """
        Возвращает название плейлиста
        :return:Название плейлиста
        """
        return self.__title


    def show_best_video(self):
        """
        Возвращает URL наиболее популярного видео в плейлисте
        :return:URL наиболее популярного видео в плейлисте
        """
        best_video = max(self.__videos, key=lambda i: i.likes_count)
        return f'https://youtu.be/{best_video.video_id}'

    def video_ids(self):
        """
        Возвращает список идентификаторов видео в плейлисте
        :return:Список идентификаторов видео в плейлисте
        """
        return [video['contentDetails']['videoId'] for video in self.__info_videos['items']]

    def videos(self):
        """
        Возвращает список объектов Video, представляющих видео в плейлисте
        :return:Список объектов Video, представляющих видео в плейлисте
        """
        result = []
        for video_id in self.__video_ids:
            video = Video(video_id)
            result.append(video)
        return result

    @classmethod
    def get_service(cls):
        """
        Возвращает экземпляр клиента YouTube API
        :return:Экземпляр клиента YouTube API
        """
        return cls.youtube

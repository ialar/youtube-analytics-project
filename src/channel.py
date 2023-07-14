import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для YouTube-канала"""

    def __init__(self, channel_id: str) -> None:
        """Инициализирует экземпляр класса Channel"""
        self.__channel_id = channel_id
        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscriber_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(self.channel['items'][0]['statistics']['viewCount'])

    def __str__(self):
        """Строковое представление объекта
        (название канала и URL-адрес)"""
        return f'{self.title} ({self.url})'

    # Реализация сложения, вычитания и сравнения количества подписчиков каналов
    def __add__(self, other):
        if type(other) == Channel:
            return self.subscriber_count + other.subscriber_count
        else:
            raise TypeError

    def __sub__(self, other):
        if type(other) == Channel:
            return self.subscriber_count - other.subscriber_count
        else:
            raise TypeError

    def __gt__(self, other):
        if type(other) == Channel:
            return self.subscriber_count > other.subscriber_count
        else:
            raise TypeError

    def __ge__(self, other):
        if type(other) == Channel:
            return self.subscriber_count >= other.subscriber_count
        else:
            raise TypeError

    def __lt__(self, other):
        if type(other) == Channel:
            return self.subscriber_count < other.subscriber_count
        else:
            raise TypeError

    def __le__(self, other):
        if type(other) == Channel:
            return self.subscriber_count <= other.subscriber_count
        else:
            raise TypeError

    @property
    def channel_id(self):
        """Геттер идентификатора YouTube-канала"""
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Возвращает объект службы YouTube API для выполнения запросов"""
        api_key: str = os.getenv('YouTube_API')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        """Сохраняет в файл значения атрибутов экземпляра класса"""
        data = self.__dict__
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

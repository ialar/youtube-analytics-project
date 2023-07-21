import os

from googleapiclient.discovery import build


class BaseYouTubeService:
    """Базовый класс для реализации запросов через YouTube API"""

    def __init__(self):
        api_key: str = os.getenv('YouTube_API')
        self.api = build('youtube', 'v3', developerKey=api_key)

from datetime import timedelta

import isodate

from src.base_yt_api_service import BaseYouTubeService


class PlayList(BaseYouTubeService):
    """Класс для плейлиста"""

    def __init__(self, playlist_id: str):
        """Инициализирует экземпляр класса PlayList"""
        super().__init__()
        self.__playlist_id = playlist_id
        self.playlist_videos = self.api.playlistItems(). \
            list(playlistId=playlist_id, part='snippet,contentDetails,id,status', maxResults=50).execute()
        self.title = self.playlist_videos['items'][0]['snippet']['title'].split(".")[0]
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'
        self.__videos = []
        self.get_playlist_data()

    @property
    def videos(self):
        """Геттер списка видеороликов в плейлисте"""
        return self.__videos

    def get_playlist_data(self):
        """Собирает данные о плейлисте с помощью YouTube API"""
        video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        videos = self.api.videos(). \
            list(part='contentDetails,statistics', id=','.join(video_ids)).execute()
        self.__videos = videos['items']

    @property
    def playlist_id(self) -> str:
        """Геттер идентификатора плейлиста"""
        return self.__playlist_id

    @property
    def total_duration(self) -> timedelta:
        """Геттер общей длительности плейлиста"""
        total_duration = timedelta()
        for video in self.videos:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """Возвращает ссылку на лучшее (по количеству лайков) видео из плейлиста"""
        best_video = max(self.videos, key=lambda video: video['statistics']['likeCount'])
        video_id = best_video['id']
        return f'https://youtu.be/{video_id}'

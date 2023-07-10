from src.channel import Channel


class Video:
    """Класс для YouTube-видео"""

    def __init__(self, video_id: str):
        """Инициализирует экземпляр класса Video."""
        # super().__init__(channel_id="UC-OVMPlMA3-YCIeg4z5z23A")
        self.__video_id = video_id
        self.video = Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=video_id
                                                         ).execute()
        self.title = self.video['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={video_id}'
        self.view_count = int(self.video['items'][0]['statistics']['viewCount'])
        self.like_count = int(self.video['items'][0]['statistics']['likeCount'])

    def __str__(self) -> str:
        """Строковое представление объекта
        (название видео)"""
        return self.title

    @property
    def video_id(self) -> str:
        """Геттер идентификатора YouTube-видео."""
        return self.__video_id


class PLVideo(Video):
    """Подкласс для видео в плейлисте"""

    def __init__(self, video_id: str, playlist_id: str):
        """Инициализирует экземпляр класса PLVideo."""
        super().__init__(video_id)
        self.playlist_id = playlist_id

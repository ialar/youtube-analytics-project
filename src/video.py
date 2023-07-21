from src.channel import Channel


class Video:
    """Класс для YouTube-видео"""

    def __init__(self, video_id: str) -> None:
        """Инициализирует экземпляр класса Video"""
        self.__video_id = video_id
        self.video_response = None
        self.title = None
        self.url = None
        self.view_count = None
        self.like_count = None
        self.get_video_data()

    def __str__(self) -> str:
        """Возвращает строковое представление объекта
        (название видео)"""
        return self.title

    def get_video_data(self) -> None:
        """Получает данные о видео с помощью API, заполняя атрибуты объекта
        (дополнительно обрабатывает ошибку передачи несуществующего id видео)"""
        try:
            self.video_response = Channel.get_service().videos(). \
                list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()
            self.title = self.video_response['items'][0]['snippet']['title']
            self.url = f'https://www.youtube.com/watch?v={self.video_id}'
            self.view_count = int(self.video_response['items'][0]['statistics']['viewCount'])
            self.like_count = int(self.video_response['items'][0]['statistics']['likeCount'])
        except IndexError:
            print('Такого видео не существует. Проверьте его id.')

    @property
    def video_id(self) -> str:
        """Геттер идентификатора видео"""
        return self.__video_id

    @video_id.setter
    def video_id(self, value) -> None:
        """Сеттер для идентификатора видео"""
        self.__video_id = value


class PLVideo(Video):
    """Подкласс для видео в плейлисте"""

    def __init__(self, video_id: str, playlist_id: str):
        """Инициализирует экземпляр класса PLVideo"""
        super().__init__(video_id)
        self.playlist_id = playlist_id

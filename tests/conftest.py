import pytest

from src.video import Video, PLVideo


@pytest.fixture
def video():
    return Video('AWX4JnAnjBE')


@pytest.fixture
def pl_video():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')

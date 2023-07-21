def test_video(video):
    assert video.video_id == "AWX4JnAnjBE"
    assert video.title == "GIL в Python: зачем он нужен и как с этим жить"


def test_pl_video(pl_video):
    assert pl_video.video_id == "4fObz_qw9u4"
    assert pl_video.playlist_id == "PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC"
    assert pl_video.title == 'MoscowPython Meetup 78 - вступление'


def test_broken_video(broken_video):
    assert broken_video.title is None
    assert broken_video.like_count is None

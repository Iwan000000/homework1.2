import pytest
from src.video import Video


def test_video_title():
    video = Video("AWX4JnAnjBE")
    assert video.title == "GIL в Python: зачем он нужен и как с этим жить"

def test_video_view_count():
    video = Video("AWX4JnAnjBE")
    assert video.view_count != 55280

def test_video_likes_count():
    video = Video("AWX4JnAnjBE")
    assert int(video.likes_count) == 2348

def test_video_url():
    video = Video("AWX4JnAnjBE")
    video.url = "https://youtube.com/Moscow"
    assert video.url == "https://youtube.com/Moscow"

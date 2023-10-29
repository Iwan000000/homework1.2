from datetime import timedelta
import pytest
from src.playlist import PlayList
from src.video import Video


@pytest.fixture(scope="module")
def playlist():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')

def test_playlist_title(playlist):
    assert playlist.title == 'Moscow Python Meetup №81'

def test_playlist_url(playlist):
    assert playlist.url == 'https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw'

def test_total_duration(playlist):
    expected_duration = timedelta(seconds=6592)
    assert playlist.total_duration == expected_duration

def test_show_best_video(playlist):
    assert playlist.show_best_video() == 'https://youtu.be/cUGyMzWQcGM'

def test_video_ids(playlist):
    assert playlist.video_ids() == ['feg3DYywNys', 'MtWXwMCAApY', 'nApYYXYL9qA', 'cUGyMzWQcGM']

def test_videos(playlist):
    expected_number_of_videos = 4
    videos = playlist.videos()
    assert len(videos) == expected_number_of_videos

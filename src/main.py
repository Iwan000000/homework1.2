import datetime
from item import Channel
from src.video import Video, PLVideo
from src.playlist import PlayList


if __name__ == '__main__':
    broken_video = Video('broken_video_id')
    assert broken_video.title is None
    assert broken_video.like_count is None
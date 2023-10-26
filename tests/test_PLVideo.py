import pytest
from src.video import PLVideo


def test_plvideo_title():
    plvideo = PLVideo("4fObz_qw9u4", "PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC")
    assert plvideo.title == "MoscowPython Meetup 78 - вступление"

def test_plvideo_playlist_id():
    plvideo = PLVideo("4fObz_qw9u4", "PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC")
    assert plvideo.playlist_id == "PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC"
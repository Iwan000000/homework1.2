import pytest
from src.item import Channel

@pytest.fixture
def channel():
    channel_id = "UC4yHMRbOxXJA6DfqXk0Y4Aw"
    return Channel(channel_id)


def test_print_info(channel, capsys):
    channel.print_info()
    captured = capsys.readouterr()
    assert "Название канала" in captured.out
    assert "Описание канала" in captured.out
    assert "Страна" in captured.out

def test_no_api_key():
    with pytest.raises(Exception):
        channel = Channel("UC4yHMRbOxXJA6DfqXk0Y4Aw")

def test_invalid_channel_id():
    with pytest.raises(Exception):
        channel = Channel("invalid_channel_id")
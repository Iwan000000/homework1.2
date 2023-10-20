import pytest
import os
from src.item import Channel
import json

channel_id = "UC-OVMPlMA3-YCIeg4z5z23A"
channel = Channel(channel_id)
channel_id_2 = 'UCwHL6WHUarjGfUM_586me8w'
channel_2 = Channel(channel_id_2)
def test_channel_initialization(channel):
    assert channel.channel_id == channel_id
    assert channel.channel_name != ""
    assert channel.description != ""
    assert channel.channel_link != ""
    assert channel.subscriber_count >= 0
    assert channel.video_count >= 0
    assert channel.view_count >= 0

# Тестирование метода to_json()
def test_to_json(channel):
    filename = "channel_data.json"
    channel.to_json(filename)
    assert os.path.exists(filename)
    with open(filename) as file:
        data = json.load(file)
    assert data["channel_id"] == channel_id
    assert data["channel_name"] == channel.channel_name
    assert data["description"] == channel.description
    assert data["channel_link"] == channel.channel_link
    assert data["subscriber_count"] == channel.subscriber_count
    assert data["video_count"] == channel.video_count
    assert data["view_count"] == channel.view_count
    os.remove(filename)

@pytest.fixture
def channel():
    return Channel(channel_id)

def test_str_method(channel):
    assert str(channel) == "MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)"

def test_add_method(channel):
    highload = Channel(channel_id_2)
    result = channel + highload
    assert result

def test_sub_method(channel):
    highload = Channel(channel_id_2)
    result = channel - highload
    assert result

def test_eq_method(channel):
    highload = Channel(channel_id_2)
    assert channel != highload

def test_lt_method(channel):
    highload = Channel(channel_id_2)
    assert channel < highload

def test_ge_method(channel):
    highload = Channel(channel_id_2)
    assert channel <= highload

def test_le_method(channel):
    highload = Channel(channel_id_2)
    assert channel <= highload

def test_gt_method(channel):
    highload = Channel(channel_id_2)
    assert highload > channel
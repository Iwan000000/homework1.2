import pytest
import os
from src.item import Channel
import json

channel_id = "UC4yHMRbOxXJA6DfqXk0Y4Aw"
channel = Channel(channel_id)

def test_channel_initialization():
    assert channel.channel_id == channel_id
    assert channel.channel_name != ""
    assert channel.description != ""
    assert channel.channel_link != ""
    assert channel.subscriber_count >= 0
    assert channel.video_count >= 0
    assert channel.view_count >= 0

# Тестирование метода to_json()
def test_to_json():
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

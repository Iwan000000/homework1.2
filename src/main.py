from item import Channel

if __name__ == "__main__":
    channel_id = "UC4yHMRbOxXJA6DfqXk0Y4Aw"
    channel = Channel(channel_id)

    # Вывести данные о канале
    print("ID канала:", channel.channel_id)
    print("Название канала:", channel.channel_name)
    print("Описание канала:", channel.description)
    print("Ссылка на канал:", channel.channel_link)
    print("Количество подписчиков:", channel.subscriber_count)
    print("Количество видео:", channel.video_count)
    print("Общее количество просмотров:", channel.view_count)

    # Сохранить данные канала в файл
    channel.to_json("channel_data.json")
if __name__ == '__main__':
    # Создаем два экземпляра класса
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')
    print(highload)
    print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(moscowpython + highload)  # 100100
    print(moscowpython - highload)  # -48300
    print(highload - moscowpython)  # 48300
    print(moscowpython > highload)  # False
    print(moscowpython >= highload)  # False
    print(moscowpython < highload)  # True
    print(moscowpython <= highload)  # True
    print(moscowpython == highload)  # False





from pytube import YouTube
from pytube.contrib.session import extract


# URL YouTube-видео
video_url = "https://youtu.be/615U7p3ttE4"

# Извлекаем cookies из браузера
cookies = extract.get_ytplayer_config(video_url)['args']['cookies']

# Создаем объект YouTube с использованием cookies
yt = YouTube(video_url, cookies=cookies)

# Выбираем наилучшее доступное видео качества (MP4)
video_stream = yt.streams.filter(file_extension="mp4").get_highest_resolution()

# Скачиваем видео
video_stream.download(filename="video.mp4")




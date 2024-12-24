# Практика 1.2
import requests
import threading
import queue

ACCESS_TOKEN = '--- access_token ---'
RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
GENIUS_API_URL = 'https://api.genius.com/search'
GENIUS_URL = 'https://genius.com'

# genre = requests.get(RANDOM_GENRE_API_URL).json()

# data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
# print(data.json())
# https://genius.com/songs/9628444/apple_music_player
# res = data.json()
# song_id = res['response']['hits'][0]['result']['api_path']
# print(f'{GENIUS_URL}{song_id}/apple_music_player')

all_songs = []


class GetGenre(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        genre = requests.get(RANDOM_GENRE_API_URL).json()
        self.queue.put(genre)


class Genius(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        genre = self.queue.get()
        data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
        res = data.json()
        try:
            song_id = res['response']['hits'][0]['result']['api_path']
            all_songs.append(f'{GENIUS_URL}{song_id}/apple_music_player')
        except IndexError as e:
            # self.run()
            pass


queue = queue.Queue()
# genre_thread = GetGenre(queue)
# genius_thread = Genius(queue)

# genre_thread.start()
# genius_thread.start()

# genre_thread.join()
# genius_thread.join()

genre_list = []
genius_list = []

for _ in range(10):
    t = GetGenre(queue)
    t.start()
    genre_list.append(t)

for _ in range(10):
    t = Genius(queue)
    t.start()
    genius_list.append(t)

for t in genius_list:
    t.join()

print(all_songs)
print(len(all_songs))

import pytube

# pytube uses streams. Streams support quality up to 720p 60fps
# tested with this URL -> https://www.youtube.com/watch?v=FokeqDBelqI

link = input('Enter YouTube Video URL => ')
yt = pytube.YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()
print(f'Downloaded {stream.default_filename}')

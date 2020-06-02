from pytube import *

def playlist():
	playlist = Playlist(input("Enter the Url: "))
	print('Number of videos in playlist: {}'.format(len(playlist.video_urls)))
	for url in playlist.video_urls:
		print("Downloading: ",url)
		YouTube(url).streams.get_highest_resolution().download()

def main():
	playlist()

main()
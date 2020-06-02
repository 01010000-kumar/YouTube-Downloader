from pytube import *

def playlist(option):
	playlist = Playlist(input("Enter the Url: "))
	print('Number of videos in playlist: {}'.format(len(playlist.video_urls)))
	for url in playlist.video_urls:
		print("Downloading: ",url)
		if option == 1:
			YouTube(url).streams.get_highest_resolution().download()
		elif option == 2:
			YouTube(url).streams.filter(only_audio=True)[-1].download()

def video(option):
	url = YouTube(input("Enter the Url: "))
	if option == 1:
		url.streams.get_highest_resolution().download()
		elif option == 2:
			url.streams.filter(only_audio=True)[-1].download()


def main():
	option1 = input("What do you want to download: \n[1] Video \n[2] Playlist")
	option2 = input("Do you want it to be Audio or Original: \n[1] Original \n[2] Audio")
	if option1 == "1":
		if option2 == "1":
			video(1)
		elif option2 == "2":
			video(2)
	elif option1 == "2":
		if option2 == "1":
			playlist(1)
		elif option2 == "2":
			playlist(2)

main()
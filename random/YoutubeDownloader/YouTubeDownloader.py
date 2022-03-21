from pytube import YouTube
link = input("Enter the link of the video: ")
yt = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))
for i in video:
    print(i)
print('enter format of the video')
dn_option = int(input())
dn_video = videos[dn_option]
dn_video.download('D:\Videos')
print('video downloaded')

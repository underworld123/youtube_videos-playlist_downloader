import pytube
#pytube module contain YouTube class
#yt represent a single youtube session
#we can get the name of video by yt.filename and id by yt.video_id
#We can get a list of the available videos for download by get_videos

print("Entern\n1 => To download a video\n2 => To download a playlist")
ch=int(raw_input(">>"))
if(ch==1):
	print("Enter video url")
	link=raw_input(">>")

	yt=pytube.YouTube(link)
	print()
	#print(type(yt))
	#print(dir(yt))

	stream=yt.streams.first()
	print("Enter the Destination folder or press Enter to download in current folder")
	dt=raw_input(">>")
	if len(dt)==0:
		stream.download('.')
	else:
		stream.download(dt)

	print(yt.filename+" is downloaded")
else:
	print("Enter the playlist url")
	link=raw_input(">>")
	link=link+"&index="
	print(link)
	print("Enter the total number of videos")
	n=int(raw_input(">>"))
	print("Enter the Destination folder or press Enter to download in current folder")
	dt=raw_input(">>")
	if len(dt)==0:
		dt='.'
	yt=[0]*n
	for i in range(1,n):
		ss=link+str(i+1)
		print(ss)
		yt[i]=pytube.YouTube(ss)
		stream=yt[i].streams.first()
		stream.download(dt)

	print("Playlist is downloaded")
from pytube import YouTube

video=YouTube('https://www.youtube.com/watch?v=PD_AtXqsRo4')
print("infos: \n","titulo:",video.title,"\n","Canal:",video.author,"\n","Data_publicacao:",video.publish_date,
"\n","Views:",video.views)
video.streams.filter(progressive=True,only_audio=True)
video.streams.order_by('resolution')
#video.streams.first().download("pytube/downloads")
print("finalizado")
from pytube import YouTube
import os.path

def combine_audio(vidname, audname, outname, fps=25):
    import moviepy.editor as mpe
    
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, temp_audiofile='temp-audio.m4a', remove_temp=True, fps=fps, codec='libx264', audio_codec='aac')

print('Audio quality is always the best.')
quality = input('Video quality: ')
url = input('url: ')

yt = YouTube(url)
stream_list = yt.streams


video_bool = False
audio_bool = False

for i in range(len(stream_list)):

    if quality in str(stream_list[i]) and video_bool == False:
        stream_list[i].download(filename = 'video')
        video_bool == True
    
    if 'audio' in str(stream_list[i]) and audio_bool == False:
        stream_list[i].download(filename ='audio')
        audio_bool = True

while(True):
    
        if os.path.isfile('audio.mp4') and os.path.isfile('video.mp4'):
            break

combine_audio('video.mp4', 'audio.mp4', 'out.mp4', fps = 30)

os.remove('audio.mp4')
os.remove('video.mp4')


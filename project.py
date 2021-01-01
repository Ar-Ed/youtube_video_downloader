from pytube import YouTube
import os.path
import re

def combine_audio(vidname, audname, outname, fps=30):
    import moviepy.editor as mpe
    
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname, temp_audiofile='temp-audio.m4a', remove_temp=True, fps=fps, codec='libx264', audio_codec='aac')


url = input('url: \n')

yt = YouTube(url)
stream_list = yt.streams

video_list = set()
audio_list = set()

for i in stream_list:
    
    try:
        if i.includes_audio_track:
            audio_list.add(int(re.findall('[0-9]+(?=kbps)',str(i))[0]))
        if i.includes_video_track:    
            video_list.add(int(re.findall('[[0-9]+(?=p)',str(i))[0]))    
    except: 
        continue

print(f'Video qualities:{sorted(video_list,reverse=True)}', f'\n\nAudio qualities: {sorted(audio_list,reverse=True)}')
video_quality = input('Prefered Video quality: ') + 'p'
audio_quality = input('Prefered Audio quality: ') + 'kbps'
output_video_format = input('Prefered output format: ')
##%%

video_bool = False
audio_bool = False

for i in stream_list:

    if video_quality in str(i) and video_bool == False:
        i.download(filename = 'video')
        video_format = i.subtype
        video_bool = True
    
    if audio_quality in str(i) and audio_bool == False:
        i.download(filename ='audio')
        audio_format = i.subtype
        audio_bool = True
        
    if video_bool and audio_bool:
        break

audio_file = 'audio.' + audio_format
video_file = 'video.' + video_format

while(True):
    
        if os.path.isfile(audio_file) and os.path.isfile(video_file):
            break

combine_audio(video_file, audio_file, 'out.'+output_video_format)

try:
    os.remove(video_file)
    os.remove(audio_file)
    os.remove('video.webm')
except:
    pass




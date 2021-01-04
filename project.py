from pytube import YouTube
import os.path
import re

def video_search(video_name):
    from youtubesearchpython import VideosSearch
    
    allSearch = VideosSearch(video_name, limit = 12).result()
    
    j=1
    for i in allSearch['result']:
        print(j, i['title'], 'Duration:', i['duration'])
        j+=1
        
    print('\n0 to search again')
    rank = int(input("Rank of the prefered video: "))
    
    if rank == 0:
        return video_search(input('\nType Youtube search:'))
    
    return allSearch['result'][rank - 1]['link']


user_search = input('\nType Youtube search or url: ')

if 'youtube.com' in user_search:
    url = user_search
else:
    url = video_search(user_search)

print(f'\nDownloading {url}')

path = input('\nPath you want to install (example: /Users/your_name/):')

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
    except: continue

print(f'\nVideo qualities:{sorted(video_list,reverse=True)}', f'\n\nAudio qualities: {sorted(audio_list,reverse=True)}')
video_quality = input('Prefered Video quality: ') + 'p'
audio_quality = input('Prefered Audio quality: ') + 'kbps'
output_video_format = input('Prefered output format: ')
video_name = ''.join([i for i in (yt.title ) if  i.isalnum() or i==' ']).replace(' ','_') + '.'+output_video_format

print(video_name)

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
output = f'output.{output_video_format}'

while(True):
    
        if os.path.isfile(audio_file) and os.path.isfile(video_file):
            break

os.system(f"ffmpeg -i {video_file} -i {audio_file} -y -vcodec copy {output}")
os.system(f'mv {output} {video_name}')
os.system(f'mv {video_name} {path}')

try:
    os.remove(video_file)
    os.remove(audio_file)
    os.remove('video.webm')

except:
    pass

print('"done" to quit')
if input().lower() == 'done':
    quit()




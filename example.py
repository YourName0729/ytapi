import youtube_dl
import shutil
import json

def yt2m4a(title, video_url):
    ydl_opts = {
        'outtmpl': '{}.%(ext)s'.format(title),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    return './{0}.m4a'.format(title)

def main():
    url = input('[Input] Youtube URL: ')
    title = input('[Input] Title: ')

    fname = yt2m4a(title, url)
    destn = ''

    print('[Json] Retrieving destination')
    with open('./personal.json', 'r') as jfile:
        destn = json.load(jfile)['destination']

    print('[Shutil] Moveing file. destination: {}'.format(destn))
    shutil.move(fname, destn)

if __name__ == '__main__':
    main()
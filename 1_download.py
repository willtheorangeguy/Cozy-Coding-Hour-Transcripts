"""
This script uses yt-dlp to download videos, by year,
from the Cozy Coding Hour podcast.
"""

import yt_dlp

def download_playlist(playlist_url):
    """
    Downloads all videos from a YouTube playlist.
    """
    ydl_opts = {
        'format': 'bv+ba',
        'outtmpl': '%(upload_date>%Y)s/%(title)s.%(ext)s',
        'noplaylist': False,
        'ignoreerrors': True,
        'download_archive': 'downloaded.log',
        'remote_components': 'ejs:github',
        'concurrent_fragments': True,
        'no_mtime': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist = "https://www.youtube.com/playlist?list=PLep05UYkc6wTahxWrTdkowMic3o4612JK"
    download_playlist(playlist)
    print("Downloaded all videos from the Cozy Coding Hour podcast.")

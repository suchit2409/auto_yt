# Import the necessary libraries
import os
import youtube_dl
def vidownload(url):
# Set the YouTube channel URL
    channel_url = url

    # Set the download directory
    download_dir = './videos'

    # Create the download directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Set the download options
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'ignoreerrors': True,

    }
    
 
    # Create a YouTube Downloader object
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    # Download the videos from the YouTube channel
    with ydl:
        result = ydl.extract_info(channel_url, download=True)
        # print(result)

    



# vidownload("https://www.youtube.com/@StreetCanv2")
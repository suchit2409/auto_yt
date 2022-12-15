import os
download_dir = './videos'
ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'ignoreerrors': True,

    }
print(ydl_opts['outtmpl'])
import yt_dlp
from pathlib import Path

def download_audio(url, download_path):
    download_path = Path(download_path)
    download_path.mkdir(parents=True, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'quiet': True,  # Suppress all output
        'no_warnings': True,  # Suppress warnings
    }

    print("\nDownloading mp3 audio format...")
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_video(url, download_path):
    download_path = Path(download_path)
    download_path.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
        'no_post_overwrites': True,
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'quiet': True,  # Suppress all output
        'no_warnings': True,  # Suppress warnings
    }

    print("\nDownloading mp4 video format...")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


downloads_folder = Path.home() / "Downloads"
choice = ""

while choice not in ["1", "2"]:
    print(f"""Default download path: {downloads_folder}
    
Choose a format:
1. mp3
2. mp4
""")
    choice = input("Choice: ")

    if choice in ["1", "2"]:
        input_url = input("Enter a URL: ")

        if choice == "1":
            download_audio(input_url, downloads_folder)
        elif choice == "2":
            download_video(input_url, downloads_folder)

    else:
        print("""
Wrong input.
Please try again:
""")

.PHONY: build

build:
	pyinstaller --onedir --collect-all yt-dlp .\yt_dlp_helper.py -y
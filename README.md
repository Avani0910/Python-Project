📌 Python YouTube Downloader

A simple and powerful Python tool that allows users to download YouTube videos in MP4 (video) or MP3 (audio) format. Built using the pytube library, this downloader provides flexible format options and fast downloading for offline use.

📘 Introduction

The Python YouTube Downloader is designed to help users download YouTube videos or extract audio from them. Whether you want to save lectures, music, tutorials, or entertainment videos, this tool lets you choose between MP4 video download or MP3 audio extraction. It is easy to use, reliable, and ideal for students and everyday users.

🛠️ Features

✔ Download videos in MP4 format
✔ Download audio in MP3 format
✔ Simple and clean command-line interface
✔ Uses pytube for smooth downloads
✔ Error handling for invalid URLs & connectivity issues
✔ Fast and lightweight

⚙️ Technologies Used

Python

Pytube library

🚀 How It Works

User enters a YouTube video URL

User selects a format: MP4 video or MP3 audio

The program fetches available streams using pytube

Selected format is downloaded and saved locally



✅ Improved Python YouTube Downloader Code (MP3 + MP4)
from pytubefix import YouTube

# Ask user for a YouTube video URL
url = input("Enter the YouTube video link: ").strip()

try:
    yt = YouTube(url)

    # Ask user for download type
    choice = input("Enter download type (mp3/mp4): ").strip().lower()

    if choice == "mp3":
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_file = audio_stream.download()
        print("\n✅ MP3 Download Complete!")
        print("Saved as:", output_file)

    elif choice == "mp4":
        video_stream = yt.streams.get_highest_resolution()
        output_file = video_stream.download()
        print("\n🎥 MP4 Download Complete!")
        print("Saved as:", output_file)

    else:
        print("\n❌ Invalid choice! Please enter 'mp3' or 'mp4'.")

except Exception as e:
    print("\n⚠️ Error occurred:", e)

⭐ Improvements Made

Here’s what I improved in your script:

✔ Dynamic URL input

Let user paste any YouTube link instead of a fixed one.

✔ Better variable naming

yt, audio_stream, video_stream, etc. for clarity.

✔ Clean console messages

Added emojis & clear status messages.

✔ Error handling

Wraps everything in a try-except block to avoid program crashing.




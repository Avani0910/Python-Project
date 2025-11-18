from pytubefix import YouTube

link = YouTube(r"https://youtu.be/HJy2Rxlv-sA?si=Hs9oxZ-E7FZW5SQJ")

# Ask user whether to download as MP3 or MP4
choice = input("Enter download type (mp3/mp4): ").strip().lower()

if choice == "mp3":
    audio_link = link.streams.filter(only_audio=True).first()
    audio_file = audio_link.download()
    print("MP3 Download Complete:", audio_file)

elif choice == "mp4":
    video_quality = link.streams.get_highest_resolution()
    video_file = video_quality.download()
    print("MP4 Download Complete:", video_file)

else:
    print("Invalid choice! Please enter 'mp3' or 'mp4'.")

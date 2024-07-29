import os

#.file Endings
audio_files = (".mp3",".wav",".flac",".aac",".ogg",".wma")
video_files = (".mpg",".mov",".wmv",".rm",".webm",".mp4")
image_files = (".jpeg",".png",".svg",".gif")
text_files = (".txt",".doc",".pdf",".rtf",".odt")

Messy_dir_path = r"" #Put full file path
Files = os.listdir(Messy_dir_path)

audio_folder = ""
video_folder = ""
image_folder = ""
text_folder = ""



import os
import shutil

#.file Endings
audio_files = (".mp3",".wav",".flac",".aac",".ogg",".wma")
video_files = (".mpg",".mov",".wmv",".rm",".webm",".mp4")
image_files = (".jpeg",".png",".svg",".gif")
text_files = (".txt",".doc",".pdf",".rtf",".odt")

def Sort_Files(Messy_dir_path,audio_folder,video_folder,image_folder,text_folder):
    Files = os.listdir(Messy_dir_path)
    for file in Files:
        index = file.find(".")
        Des_folder = ""
        if index == -1:continue
        if file[index:] in audio_files: Des_folder = audio_folder
        elif file[index:] in video_files: Des_folder = video_folder
        elif file[index:] in image_files: Des_folder = image_folder
        elif file[index:] in text_files: Des_folder = text_folder
        else:continue
        shutil.move(f"{Messy_dir_path}\\{file}",Des_folder)
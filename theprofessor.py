from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("Donloading...")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4)
    #code for mp3
    audio_file = video_clip.audio
    audio_file.write_audiofile("audio.mp3")
    audio_file.close()
    shutil.move("audio.mp3", file_path)
    #code for mp4
    video_clip.close()
    shutil.move(mp4, file_path)
    print('Download Complete')



def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


root = Tk()
root.title('The Professor - The Video Downloader 😎')
canvas = Canvas(root,width=500,height=400)
canvas.pack()
canvas.configure(bg='#5C8374')



#app label
app_label = Label(root, text='The Professor 😎',fg='#26577C',font=('Cascadia Code 25 bold', 20)).place(x=180, y=20)
canvas.create_window(200, 20, window=app_label)

#entry to accept video URL
# Create the URL label
url_label = Label(root, text="Enter Video URL 👇🏻", font='Helvetica 15 bold')

# Create the URL entry
url_entry = Entry(root, width=65)

# Place the URL label and entry
url_label.place(x=185, y=70)
url_entry.place(x=70, y=105)

canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)




#path to download videos
# Create the path label
path_label = Label(root, text="Select path to download", font='Helvetica 11 bold')

# Place the path label
path_label.place(x=180, y=130)

# Create the path button
path_button = Button(root, text='SELECT', width=10, command=get_path).place(x = 220, y = 160) 

canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=path_button)


#download button
download_button = Button(root, text='Download Video', width=20, command=download).place(x = 180, y = 250) 
canvas.create_window(200, 250, window=download_button)



root.mainloop()
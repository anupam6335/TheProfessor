from tkinter import *
from tkinter import filedialog


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
url_label = Label(root, text="Enter Video URL 👇🏻",  font='Helvetica 15 bold').place(x = 185, y = 70) 
url_entry = Entry(root, width=65).place(x = 70, y = 105) 

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
download_button = Button(root, text='Download Video', width=20).place(x = 180, y = 250) 
canvas.create_window(200, 250, window=download_button)



root.mainloop()
from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('The Professor - The Video Downloader 😎')
canvas = Canvas(root,width=500,height=400)
canvas.pack()

#app label
app_label = Label(root, text='The Professor 😎',fg='#26577C',font=('Cascadia Code 25 bold', 20)).place(x=160)
canvas.create_window(200, 20, window=app_label)

#entry to accept video URL
url_label = Label(root, text="Enter Video URL 👇🏻",  font='Helvetica 15 bold').place(x = 185, y = 70) 
url_entry = Entry(root, width=65).place(x = 70, y = 100) 

canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

root.mainloop()
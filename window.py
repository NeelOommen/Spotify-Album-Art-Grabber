from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from app import *

_file_path = ''

def trigger_collage():
    global _file_path
    url = entry0.get()
    fName = entry1.get()
    fPath = _file_path

    messagebox.showinfo(title='Working', message='Please wait till a status message indicates completion')
    window.title('Spotify Collage - Working...')
    collage(url, fPath, fName)
    window.title('Make Spotify Collages!')
    messagebox.showinfo(title='Finished!', message='Completed!')


def file_browse():
    global _file_path

    _file_path = filedialog.askdirectory()
    entry2.delete(0,END)
    entry2.insert(0,_file_path)

window = Tk()

window.geometry("600x800")
window.configure(bg = "#000000")
window.title('Make Spotify Collages!')
canvas = Canvas(
    window,
    bg = "#000000",
    height = 800,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"UI/background.png")
background = canvas.create_image(
    281.0, 530.5,
    image=background_img)

entry0_img = PhotoImage(file = f"UI/img_textBox0.png")
entry0_bg = canvas.create_image(
    294.0, 310.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 84.0, y = 276,
    width = 420.0,
    height = 66)

entry1_img = PhotoImage(file = f"UI/img_textBox1.png")
entry1_bg = canvas.create_image(
    294.0, 434.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 84.0, y = 400,
    width = 420.0,
    height = 66)

entry2_img = PhotoImage(file = f"UI/img_textBox2.png")
entry2_bg = canvas.create_image(
    198.0, 558.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 85.0, y = 524,
    width = 226.0,
    height = 66)

img0 = PhotoImage(file = f"UI/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = trigger_collage,
    relief = "flat")

b0.place(
    x = 197, y = 629,
    width = 205,
    height = 74)

img1 = PhotoImage(file = f"UI/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = file_browse,
    relief = "flat")

b1.place(
    x = 336, y = 532,
    width = 205,
    height = 52)

window.resizable(False, False)
window.mainloop()

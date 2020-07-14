import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os


def main():
    global logiN, passW
    logiN = 'login'
    passW = 'password'
    display = tk.Tk()
    display.geometry('400x400')
    log_pass(display)
    display.mainloop()

def log_pass(okno):
    login = tk.Entry(okno)
    login.grid(row = 0, column = 0)

    password = tk.Entry(okno)
    password.grid(row = 1, column = 0)
    check_btn = ttk.Button(okno, text = "Войти", command = lambda: get_key(login.get(), password.get()))
    check_btn.grid(row = 2, column = 1)

def get_key(login, password):
    if login == logiN and password == passW:
        mem_window()

def mem_window():
    mem_display = tk.Toplevel()
    dir_images = os.getcwd() + '/pic'
    dir_images = os.listdir(dir_images)
    rand_img = random.choice(dir_images)
    img = Image.open("pic/" + rand_img)

    img = ImageTk.PhotoImage(img)

    picture = tk.Label(mem_display, image=img)
    picture.grid(row=0, column=0)
    mem_display.mainloop()

if __name__ == "__main__":
    main()
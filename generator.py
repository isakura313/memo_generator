import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random


def main():
    display = tk.Tk()
    log_pass(display)
    display.mainloop()

def log_pass(okno):
    login = tk.Entry(okno)
    login.grid(row = 0, column = 0)

    password = tk.Entry(okno)
    password.grid(row = 1, column = 0)
    check_btn = ttk.Button(okno, text = "Войти", command = lambda: get_key(login.get(), password.get()))
    check_btn.grid(row = 2, column = 0)

def get_key(login, password):
    if login == 'codabra' and password == 'qwerty':
        print('okey')
        mem_window()

def mem_window():
    mem_display = tk.Toplevel()
    img = Image.open("pic/" +f"{str(random.randint(1,5))}.png")
    img = ImageTk.PhotoImage(img)

    picture = tk.Label(mem_display, image=img)
    picture.grid(row=0, column=0)
    mem_display.mainloop()

if __name__ == "__main__":
    main()
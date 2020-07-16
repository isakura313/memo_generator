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

    forget_btn = ttk.Button(okno, text= "Забыли пароль? ", command = lambda: forget_pass())
    forget_btn.grid(row =3, column = 0)

def forget_pass():
    forget_display = tk.Toplevel()

    secret_question = ttk.Combobox(forget_display, values = ("Как зовут маму", "Номер школы"))
    secret_question.grid(row = 0, column = 0)

    secret_answer = ttk.Entry(forget_display)
    secret_answer.grid(row = 1, column = 0)

    check_btn = ttk.Button(forget_display, text = "Проверить", command = lambda: answer(forget_display,
                                                                                        secret_question.get(),
                                                                                        secret_answer.get()))

    check_btn.grid(row =2, column = 0)

    def answer(okno, quest, answer):
        dict_quest = {"Как зовут маму": "Татьяна", "Номер школы": "171"}
        if dict_quest[quest] == answer:
            okno.destroy()
            new_log_pass_window = tk.Tk()
            new_log = ttk.Entry(new_log_pass_window)
            new_log.grid(row = 0, column = 0)

            new_pass = ttk.Entry(new_log_pass_window)
            new_pass.grid(row =1, column = 0) #поле нового пароля

            new_btn = ttk.Button(new_log_pass_window, text = "Новый логин и пароль")
            new_btn.grid(row = 2, column =0)
            new_log_pass_window.mainloop()
    forget_display.mainloop()


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
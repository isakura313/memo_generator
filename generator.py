import tkinter as tk
from tkinter import ttk

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

def mem_window():
    mem_display = tk.Toplevel()
    mem_display.mainloop()

if __name__ == "__main__":
    main()
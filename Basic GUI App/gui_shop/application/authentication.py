import json
from tkinter import Button, Entry, Label
from application.canvas import tk
from application.helpers import clean_screen
from application.products import render_products


def register(**user):
    user.update({'products': []})
    with open('db/users.txt', 'a') as file:
        file.write(json.dumps(user))
        file.write('\n')
    with open('db/user_credentials.txt', 'a') as file:
        file.write(f"{user.get('username')} : {user.get('password')}")
        file.write('\n')
    render_login(errors=None)


def render_register():
    clean_screen()
    Label(text='Enter Username:').grid(row=5, column=4)
    username = Entry(tk)
    username.grid(row=5, column=5)
    Label(text='Enter Password:').grid(row=6, column=4)
    password = Entry(tk, show='*')
    password.grid(row=6, column=5)
    Label(text='Enter First Name:').grid(row=7, column=4)
    first_name = Entry(tk)
    first_name.grid(row=7, column=5)
    Label(text='Enter Last Name:').grid(row=8, column=4)
    last_name = Entry(tk)
    last_name.grid(row=8, column=5)
    Button(tk, text='Register', bg='blue', fg='red',
           command=lambda: register(username=username.get(),
                                    password=password.get(),
                                    first_name=first_name.get(),
                                    last_name=last_name.get())).grid(row=9, column=5)


def login(username, password):
    with open ('db/user_credentials.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            user, passw = line[:-1].split(' : ')
            if user == username and passw == password:
                with open("db/current_user.txt", "w") as user_file:
                    user_file.write(username)
                render_products()
                return
        render_login(errors=True)


def render_login(errors=None):
    clean_screen()
    Label(text='Enter Username:').grid(row=4, column=5)
    username = Entry(tk)
    username.grid(row=5, column=5)
    Label(text='Enter Password:').grid(row=4, column=7)
    password = Entry(tk, show='*')
    password.grid(row=5, column=7)
    Button(tk, text='Login', bg='blue', fg='orange', command=lambda :login(username=username.get(), password=password.get())).grid(row=7, column=7)
    if errors:
        Label(text='Invalid username or password').grid(row=8, column=5)



def render_main_enter_screen():
    Button(tk, text='Login', bg='green', fg='red', command=render_login).grid(row=5, column=5)
    Button(tk, text='Register', bg='yellow', fg='red', command=render_register).grid(row=5, column=7)

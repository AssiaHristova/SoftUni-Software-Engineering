import json
import os
from PIL import Image, ImageTk
from tkinter import Button, Label
from application.helpers import clean_screen
from application.canvas import tk

base_folder = os.path.dirname(__file__)


def buy_product(button):
    _, product_id = button.cget("text").split()
    product_id = int(product_id)
    current_logged_user = None
    with open("db/current_user.txt", "r") as file:
        current_logged_user = file.readline()
    with open("db/users.txt", "r+") as users_file:
        users = users_file.readlines()
        users_file.seek(0)
        for user in users:
            user_as_dict = json.loads(user)
            if user_as_dict.get("username") == current_logged_user:
                user_as_dict["products"].append(product_id)
            users_file.write(json.dumps(user_as_dict))
            users_file.write("\n")
    with open("db/products.txt", "r+") as products_file:
        products = products_file.readlines()
        products_file.seek(0)
        for product in products:
            product_as_dict = json.loads(product)
            if product_as_dict.get("id") == product_id:
                product_as_dict["count"] -= 1
            products_file.write(json.dumps(product_as_dict))
            products_file.write("\n")
    render_products()


def render_products():
    clean_screen()
    with open ('db/products.txt', 'r') as file:
        products = file.readlines()
        column_counter = 0
        for product in products:
            current_product = json.loads(product)

            Label(tk, text=current_product.get('name')).grid(row=1, column=column_counter)

            image = Image.open(os.path.join(os.path.join(base_folder, "db/images"), current_product.get("img_path")))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=2, column=column_counter)

            Label(tk, text=current_product.get("count")).grid(row=3, column=column_counter, pady=2)
            button = Button(tk, text=f"Buy {current_product.get('id')}")
            button.configure(command=lambda b=button: buy_product(b))
            button.grid(row=4, column=column_counter)

            column_counter += 1





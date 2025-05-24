
import tkinter
from tkinter import PhotoImage
from fernet import Fernet
from tkinter import messagebox
import base64
import hashlib

window = tkinter.Tk()
window.config(width=800,height=800,padx=50,pady=50)
window.title("Secret Notes")



master_key_entry= tkinter.Entry()
secret_text= tkinter.Text(height=10,width=30)






def cryptography():
    key2 = master_key_entry.get()
    key1 =hashlib.sha256(key2.encode()).digest()
    key_son = base64.urlsafe_b64encode(key1)
    f = Fernet(key_son)

    mesaj2 = secret_text.get("1.0","end-1c")
    mesaj = mesaj2.encode("utf-8")
    sifreli = f.encrypt(mesaj)

    if title_entry.get() =="":
        tkinter.messagebox.showerror("showerror","Please enter your title!")
    elif master_key_entry.get() == "":
        tkinter.messagebox.showerror("showerror","Set your password!")
    elif secret_text.get("1.0", "end-1c") == "" :
        tkinter.messagebox.showerror("showerror","Set your secret!")

    else:
        with open("sifres.txt",mode="a") as myFile:
            myFile.write(f'''{title_entry.get()}"
        {sifreli.decode()}             
    ''')
        onay_label= tkinter.Label(text= "Your password is stored")
        onay_label.pack()

        with open("kripto and password.txt",mode="a") as file:
            file.write(f'''{sifreli.decode()}{master_key_entry.get()}
        Anahtar = {key_son}
    '''               )


def decryption():
    mesaj2 = secret_text.get("1.0","end-1c")
    mesaj = mesaj2.encode("utf-8")
    key2 = master_key_entry.get()
    key1 =hashlib.sha256(key2.encode()).digest()
    key_son = base64.urlsafe_b64encode(key1)
    f = Fernet(key_son)
    try:
        cozulen = f.decrypt(mesaj)
    except:
        cozulen = 0
    with open("kripto and password.txt",mode="r") as read:
        icerik = read.read()
        if master_key_entry.get() == "":
            tkinter.messagebox.showerror("showerror", "Please enter your Password!")
        elif secret_text.get("1.0", "end-1c") == "":
            tkinter.messagebox.showerror("showerror", "Please enter your encrypted password!")
        elif type(cozulen) == int:
            tkinter.messagebox.showerror("showerror","Your password or encrypted secret is wrong!")
        elif f"{secret_text.get("1.0","end-1c")}{master_key_entry.get()}" in icerik:
            tkinter.messagebox.showinfo("Info",f"Your password {cozulen.decode()}")
        else:
            tkinter.messagebox.showerror("ERROR","ERROR")

resim = tkinter.PhotoImage(file="images.png")
resim_label = tkinter.Label(image = resim,padx=30,pady=30)
resim_label.pack()

title_label = tkinter.Label(text="Enter your title")
title_label.pack()

title_entry= tkinter.Entry()
title_entry.pack()

secret_label = tkinter.Label(text="Enter your secret")
secret_label.pack()


secret_text.pack()

master_key_label= tkinter.Label(text="Enter your master key")
master_key_label.pack()

master_key_entry.pack()

save_button = tkinter.Button(text="Save & Encrypt",command= cryptography)
save_button.pack()

decrypt_button= tkinter.Button(text= "Decrypt",command=decryption)
decrypt_button.pack()






window.mainloop()
